# Author: Nick Gogan (gogannick@gmail.com)
# Date: October 30 2023
# This is for reference/demo/workshop purposes only and is not meant to be production ready code.
# There are no warranties or guarantees associated with this code.

from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from hurry.filesize import size
from pympler import asizeof
from enum import Enum

# Needed to easily pretty-print possible IndexBy enum
class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

class IndexBy(ExtendedEnum):
    ALL = 'ALL'
    BYTES = 'BYTES'
    RECORDS = 'RECORDS'

def main():
    mongo_uri = 'mongodb+srv://<username>:<password>@<clustername>.<projecthash>.mongodb.net/?retryWrites=true' #CHANGEME
    mongo_insert_batch_size = 1_000
    mongo_reset_collection = False #This assumes there is either an empty DevDay.wikipedia collection or this collection does not exist when running this script.
    index_by = IndexBy.ALL
    embedding_model_name = 'sentence-transformers/all-MiniLM-L6-v2' # 384 dimensions
    dataset_path = 'wikipedia'
    #Tested with 20220301.en, 20220301.fr, 20220301.it, 20220301.de, 20220301.frr
    dataset_name = '20220301.en' #CHANGEME #https://huggingface.co/datasets/wikipedia
    dataset_language = 'english' #CHANGEME
    dataset_date = '20220301' #CHANGEME
    data_total_volume_in_bytes = 1.1e+7 #1.1e7 is 10MB, 1.1e+9 is 1GB, 1.1e+10 is 10GB...
    data_total_record_count = 1_000_000
    mongo_dbname = 'DevDay'
    mongo_collname = 'wikipedia'

    dataset = iter(load_dataset(dataset_path, dataset_name, split='train', streaming=True))
    encoder = SentenceTransformer(embedding_model_name)
    description = {
        'dataset_name': f'{dataset_path}/{dataset_name}',
        'dataset_date': dataset_date,
        'model_name': embedding_model_name,
        'language': dataset_language
    }
    print(description)
    
    mongo_client = create_mongo_client(mongo_uri)
    mongo_collection = mongo_client.get_database(mongo_dbname).get_collection(mongo_collname)
    if mongo_reset_collection:
        print(f'Dropping [{mongo_dbname}.{mongo_collname}]...')
        mongo_collection.drop()

    match index_by:
        case IndexBy.ALL:
            print(f'Indexing everything in [{dataset_path}/{dataset_name}].')
            index_everything(dataset, description, encoder, mongo_collection, mongo_insert_batch_size)
        case IndexBy.BYTES:
            print(f'Indexing a max of [{size(data_total_volume_in_bytes)}] from [{dataset_path}/{dataset_name}].')
            index_by_bytes(dataset, description, encoder, mongo_collection, mongo_insert_batch_size, data_total_volume_in_bytes)
        case IndexBy.RECORDS:
            print(f'Indexing a max of [{data_total_record_count}] records from [{dataset_path}/{dataset_name}].')
            index_by_record_count(dataset, description, encoder, mongo_collection, mongo_insert_batch_size, data_total_record_count)
        case _:
            print(f'Unknown indexing option [{index_by}]. Available options are: [{IndexBy.list()}].')

    print('Completed successfully!')

def index_everything(dataset, description, encoder, mongo_collection, batch_size):
    documents_buffer = []
    bytes_inserted = 0
    batch_number = 0

    dataset_entry = next(dataset, None)
    record_counter = 1
    while(dataset_entry is not None):
        doc = description | {
            'title': dataset_entry.get('title'),
            'url': dataset_entry.get('url'),
            'text': dataset_entry.get('text'),
            'vector': encoder.encode(dataset_entry.get('text')).tolist()
        }
        documents_buffer.append(doc)
        bytes_inserted += asizeof.asizeof(doc)
        record_counter += 1
        print(f'Doc [{record_counter}]. Total size so far is [{size(bytes_inserted)}].')
        if(len(documents_buffer) >= batch_size):
            print('Inserting docs...')
            print(mongo_collection.insert_many(documents_buffer, False))
            batch_number += 1
            print(f'Inserted [{size(bytes_inserted)}] as of batch [{batch_number}]. Flushing buffer..')
            documents_buffer.clear()
        
        dataset_entry = next(dataset, None)
    
    if(len(documents_buffer) > 0):
        print(f'Inserting remaining [{len(documents_buffer)}] docs from buffer..')
        print(mongo_collection.insert_many(documents_buffer, False))

def index_by_bytes(dataset, description, encoder, mongo_collection, batch_size, max_bytes: float):
    documents_buffer = []
    bytes_inserted = 0
    batch_number = 0

    dataset_entry = next(dataset, None)
    record_counter = 1
    while(bytes_inserted <= max_bytes and dataset_entry is not None):
        doc = description | {
            'title': dataset_entry.get('title'),
            'url': dataset_entry.get('url'),
            'text': dataset_entry.get('text'),
            'vector': encoder.encode(dataset_entry.get('text')).tolist()
        }
        documents_buffer.append(doc)
        bytes_inserted += asizeof.asizeof(doc)
        record_counter += 1
        print(f'Doc [{record_counter}]. Total size so far is [{size(bytes_inserted)}].')
        if(len(documents_buffer) >= batch_size):
            print('Inserting docs...')
            print(mongo_collection.insert_many(documents_buffer, False))
            batch_number += 1
            print(f'Inserted [{size(bytes_inserted)}] as of batch [{batch_number}]. Flushing buffer..')
            documents_buffer.clear()
        
        dataset_entry = next(dataset, None)

    if(len(documents_buffer) > 0):
        print(f'Inserting remaining [{len(documents_buffer)}] docs from buffer..')
        print(mongo_collection.insert_many(documents_buffer, False))

def index_by_record_count(dataset, description, encoder, mongo_collection, batch_size, max_records):
    documents_buffer = []
    bytes_inserted = 0
    batch_number = 0

    dataset_entry = next(dataset, None)
    record_counter = 1
    while(record_counter + 1 <= max_records and dataset_entry is not None):
        doc = description | {
            'title': dataset_entry.get('title'),
            'url': dataset_entry.get('url'),
            'text': dataset_entry.get('text'),
            'vector': encoder.encode(dataset_entry.get('text')).tolist()
        }
        documents_buffer.append(doc)
        bytes_inserted += asizeof.asizeof(doc)
        record_counter += 1
        print(f'Doc [{record_counter}]. Total size so far is [{size(bytes_inserted)}].')
        if(len(documents_buffer) >= batch_size):
            print('Inserting docs...')
            print(mongo_collection.insert_many(documents_buffer, False))
            batch_number += 1
            print(f'Inserted [{size(bytes_inserted)}] as of batch [{batch_number}]. Flushing buffer..')
            documents_buffer.clear()
        
        dataset_entry = next(dataset, None)

    if(len(documents_buffer) > 0):
        print(f'Inserting remaining [{len(documents_buffer)}] docs from buffer..')
        print(mongo_collection.insert_many(documents_buffer, False))

def create_mongo_client(uri: str):
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e) 

if __name__ == "__main__":
    main()