# Table of Contents
- [Table of Contents](#table-of-contents)
- [Inventory](#inventory)
- [Vectorize Query](#vectorize-query)
- [Get your own clean wikipedia dataset](#get-your-own-clean-wikipedia-dataset)

# Inventory

`wikipedia_tiny.json` is meant to be used with [`mongoimport`](https://www.mongodb.com/docs/database-tools/mongoimport/) or Compass to import data, whereas `devday.10172023.wikipedia_tiny.gz` is the same file but compressed to make it easier to transfer around. This file contains 5,000 total records of cleaned wikipedia pages in English, French, German, Italian, and Frisian. 

To import `wikipedia_tiny.json` into a cluster using a database user authenticating with SCRAM (i.e. user & password), please use [`mongoimport`](https://www.mongodb.com/docs/database-tools/mongoimport/) like this:
```bash
mongoimport 'mongodb+srv://<username>:<password>@<clustername>.<atlasProjectHash>.mongodb.net/' --file='wikipedia_tiny.json
```
To accomplish this using the Compass GUI, [follow this guide](https://www.mongodb.com/docs/compass/current/import-export/#import-data-into-a-collection).

To import `devday.10172023.wikipedia_tiny.gz` into a cluster using a databse user authenticating with SCRAM (i.e. username & password), please use [mongorestore](https://www.mongodb.com/docs/database-tools/mongorestore/) like this:
```bash
mongorestore 'mongodb+srv://<username>:<password>@<clustername>.<atlasProjectHash>.mongodb.net' --archive='devday.10172023.wikipedia_tiny.gz' --gzip
```

# Vectorize Query

1. Set up your python environment (if not done already):

```
python3 -m venv .ENV
```

```
source .ENV/bin/activate
```

```
pip install -r requirements.txt
```

2. Open a terminal session where you activated your ENV. 

3. Start python interpreter: ```python3```

4. Import HuggingFace transformers library: ```from sentence_transformers import SentenceTransformer```

5. Get handle on the ```all-MiniLM-L6-v2``` model: ```encoder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')```

6. Encode query text into vector representation: ```encoder.encode(<yourquery>).tolist()```

# Get your own clean wikipedia dataset

All code is contained within `main.py` and requirements within `requirements.txt`. The latter was produced using `pip freeze > requirements.txt`. All configuration for `main.py` is located immediately within the `main()` function near the top of the file, with comments indicated what to change. **The main requirement is to replace the `mongo_uri` variable with your [cluster's connection string](https://www.mongodb.com/docs/guides/atlas/connection-string/).**

The defaults of `main.py` are:
    - Indexing all of the clean, English language wikipedia dataset from [HuggingFace](https://huggingface.co/datasets/wikipedia). This amounts to **~16.18GB of raw data**. The python file also includes options to index by a given max bytes or max record count. Other languages are available, just visit the HuggingFace dataset link.
    - The `all-MiniLM-L6-v2` embedding model is used to vectorize the body of the each wikipedia entry. This also comes from HuggingFace and has 384 dimensions. 
    - All content is shaped into a JSON document and is inserted into the target Atlas cluster **concurrently** in batches of `1000` documents.

To run the script yourself and generate a different dataset: 

1. Set up your python environment (if not done already):

```
python3 -m venv .ENV
```

```
source .ENV/bin/activate
```

```
pip install -r requirements.txt
```

2. Update the `mongo_uri` variable with your connection string. 

3. Run the script:
```
python3 main.py
```