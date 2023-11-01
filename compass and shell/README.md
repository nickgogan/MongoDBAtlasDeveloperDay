# Compass (& Mongo Shell)

The following is a plaintext version of the exercises in the PDF presentations. It is meant to guide workshop participants through the process by providing code snippets that can be easily copy/pasted into the [MongoDB Compass GUI](https://www.mongodb.com/docs/compass/current/) and its embedded [MongoDB shell (mongosh)](https://www.mongodb.com/docs/mongodb-shell/).

Please also refer to [the PDF of the presentation](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/DevDayPresentation_Full.pdf) to see helpful screenshots to aid in completing the exercises. Answers for both the Compass GUI approach and shell approach are in the PDF. For slides originally containing GIFs, this README will provide either plaintext explanations and/or links to tutorials that walk through exactly the same process as what was captured in the GIF. 

## Checkpoint 0: Prerequisites
1. As a workshop attendee/participants, please ensure that you have followed all of the [list of prerequisites](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/tree/main#prerequisites). Then, please [install MongoDB Compass](https://www.mongodb.com/try/download/compass) and copy this repository to have access to the `wikipedia_tiny.json` file in `data/`.

## Checkpoint 1: MongoDB Query Fundamentals

1. Via the Atlas web GUI, [load up the sample dataset](https://www.mongodb.com/docs/atlas/sample-data/).


2. [Get your Atlas cluster's connection string](https://www.mongodb.com/docs/guides/atlas/connection-string/) and [connect to it using Compass](https://www.mongodb.com/docs/atlas/compass-connection/).


3. Use Compass to [create a database named `mydb` and collection named `mycoll`](https://www.mongodb.com/docs/compass/current/databases/#create-a-database) (equivalent to a table in SQL) in your Atlas cluster. No need to specify any collection properties. The first set of exercises will be done in this collection. 

Most of the remaining exercises can be completed via either the Compass GUI or via [the embedded MongoDB shell](https://www.mongodb.com/docs/compass/current/embedded-shell/#open-the-embedded-mongodb-shell).

### **Exercise 1**: Insert operations
References:
1. [Compass GUI](https://www.mongodb.com/docs/compass/current/documents/insert/)
2. Shell syntax (`{options}` is optional and not needed for this exercise):

```bash
db.<collectionName>.insertOne({key:value},{options})
```
```bash
db.<collectionName>.insertMany([{k:v},{k:v}],{options})
```

Insert the following document into `mycoll`:
```JSON
{
    "name" : {
      "first" : "John",
      "last" : "Doe" },
    "address" : [
      { "location" : "work",
        "address" : {
          "street" : "16 Hatfields",
          "city" : "London",
          "postal_code" : "SE1 8DJ"},
        "geo" : { "type" : "Point", "coord" : [
         -0.109081, 51.5065752]}
      }
  ],
  "dob" :"1977-04-01T05:00:00Z",
  "retirement_fund" : 1292815.75
}
```

### **Exercise 2**: Update operations

MongoDB is a document database, which means that it lets you nest objects in the same document as well as have arrays of fields or even other objects! You can create almost any kind of document structure and MongoDB will allow you to store and query it in an intuitive manner, using, for example, dot notation to access nested fields. For example, you can access the value of `lastName` using `name.last`.

References:
- [Compass GUI](https://www.mongodb.com/docs/compass/current/documents/modify/)
- Shell syntax:
 ```bash
 db.<collectionName>.updateOne({filter},{update},{options})
 ```
 ```bash
 db.<collectionName>.updateMany({filter},{update},{options})
 ```
`{filter}` - Which documents to update (i.e. where-clause).

`{update}` - Either a replacement or a modification.

`{options}` - Notably, `{upsert:true|false}`. If the record exists, update 
it. If not, insert the contents of `{update}` as a document if it makes sense.

> Fun fact: The shell is actually a javascript interpreter! This means you can do fun stuff like declare variables and loop through records directly in the shell, using modern javascript syntax. 

Update your document to change John Doe's `lastName` to `Bo` and include the following additional address (John's been doing well for himself!):
```JSON
{ 
  "location" : "home",
  "address" : {
    "street" : "123 ABC Street",
    "city" : "AAA",
    "postal_code" : "111111"
  }
}
```
Use the following query operators as reference (you won't need all of them for this exercise):

[set](https://www.mongodb.com/docs/manual/reference/operator/update/set/) - adds / updates fields.

[unset](https://www.mongodb.com/docs/manual/reference/operator/update/unset/) - Removes fields.

[inc](https://www.mongodb.com/docs/manual/reference/operator/update/inc/) - increments a field.

[pull](https://www.mongodb.com/docs/manual/reference/operator/update/pull/) / [push](https://www.mongodb.com/docs/manual/reference/operator/update/push/) - Removes or inserts into an array.

[convert](https://www.mongodb.com/docs/manual/reference/operator/aggregation/convert/) - Converts between data types.

### **Exercise 3**: Delete operations
References:
- [Compass GUI](https://www.mongodb.com/docs/compass/current/documents/delete/):
- Shell syntax:
```bash
db.collection.deleteOne({filter},{options})
```
```bash
db.collection.deleteMany({filter},{options})
```
`{filter}` - Which document(s) to delete (i.e. where-clause).

`{options}` - Options include things like [write concern](https://www.mongodb.com/docs/manual/reference/write-concern/) (a mongoDB parameter for durability / performance tradeoffs) collation (for language support) and hint (index hinting).

### **Exercise 4**
Now, drop (i.e. delete) `mydb` using the [Compass GUI](https://www.mongodb.com/docs/compass/current/databases/#drop-a-database).


### **Exercise 5**: Read operations (i.e. queries)
#### Shell syntax
```bash
db.<collectionName>.findOne({filter},{projection}) 
```
```bash
db.<collectionName>.find({filter},{projection})
```
Note that the latter command (`find()`), by default, returns a cursor (iterable pointer) to the documents matching the query. In the shell, you can append a `toArray()` after the `find()` to get all results at once. 
#### Useful operators
[eq (equals)](https://www.mongodb.com/docs/manual/reference/operator/query/eq/) - Similar to a normal query

[gt](https://www.mongodb.com/docs/manual/reference/operator/query/gt/)/[gte](https://www.mongodb.com/docs/manual/reference/operator/query/gte/)/[lt](https://www.mongodb.com/docs/manual/reference/operator/query/lt/)/[lte](https://www.mongodb.com/docs/manual/reference/operator/query/lte/) - Greater [and equal] / less than [and equal]: Important operators for range queries.

[in:[]](https://www.mongodb.com/docs/manual/reference/operator/query/in/) / [nin:[]](https://www.mongodb.com/docs/manual/reference/operator/query/nin/) (in / not in): Multiple value equality match

[ne](https://www.mongodb.com/docs/manual/reference/operator/query/ne/) - Not equals.

[not](https://www.mongodb.com/docs/manual/reference/operator/query/not/): Inverses the logic of whatever queries follows it.

[or](https://www.mongodb.com/docs/manual/reference/operator/query/or/): Boolean OR.

[and](https://www.mongodb.com/docs/manual/reference/operator/query/and/): Boolean AND, usually used for specific nesting situations.

[exists](https://www.mongodb.com/docs/manual/reference/operator/query/exists/): Filters based on the existence of a given field. Note that a field with value `NULL` counts as existing! Personally, I can recall being `NULL` a couple of times in my life. 

[type](https://www.mongodb.com/docs/manual/reference/operator/query/type/): Filters based on [BSON type](https://www.mongodb.com/docs/manual/reference/bson-types/).

[elemMatch](https://www.mongodb.com/docs/manual/reference/operator/query/elemMatch/): Query on objects in arrays.

#### Setup
Before proceeding to the exercise, switch to using the `sample_mflix` database's `movies` collection. If following using the shell, use the `use` keyword ([Reference](https://www.mongodb.com/docs/compass/current/embedded-shell/#use-the-embedded-mongodb-shell)).
> Notice how the Compass shell provides suggestions (i.e. intellisense)!

#### Exercise
1. Find 1 movie with the title “Blacksmith Scene”.
2. Find movies released in 1991 with Brad Pitt.
3. Find all movies released after 1991.
4. Find all records where the runtime fields does not exist.
5. Find all movies where the Rotten Tomatoes rating is greater than 3.4.

[Example of how to query via the Compass GUI](https://www.mongodb.com/docs/compass/current/documents/view/).

### **Exercise 6**: Sort, Limit, Skip, Project

Below doubles as both example shell syntax as well as a short explanation of what the operators do. Don't worry Compass GUI fans, just hit the `Options` button as show in the screenshot below to get the same options:
![open Compass query options](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass/images/Compass_QueryOptions.png)


`db.<collectionName>.find({filter})`: Returns a cursor (iterable pointer to many documents). [Compass GUI example](https://www.mongodb.com/docs/compass/current/query/filter/#set-query-filter).

`db.<collectionName>.find({filter},{projection})`: Also returns a cursor to the matching documents, but provides only the specified fields. This is similar to a select-clause in SQL. Example: `db.movies.find({title: “Regeneration”}, {_id: 0, title: 1, fullplot: 1})`. Here, `0` means do NOT include the field and `1` means include it. Any field not explicitly set in the projection will be left out. By default, `_id` is always returned unless you explicitly say not to. This is because `_id` is the primary key whose global uniqueness is useful in most circumstances. [Compass GUI example](https://www.mongodb.com/docs/compass/current/query/project/).

`db.<collectionName>.find({filter},{projection})`.sort([{‘<fieldName>’:<1|-1>}]): Works the same way as the sort-clause in SQL, with `1` being `ASC` and `-1` being `DESC`.

`db.<collectionName>.find({filter},{projection}).skip(<int>)`: Works the same way as the skip-clause in SQL, with `<int>` specifying the number of records the cursor should move past the matching records before getting returned to the client.

`db.<collectionName>.find({filter},{projection}).skip().limit(<int>)`: Works the same way as as the limit-clause in SQL, with `<int>` specifying the number of records that the cursor will be able to iterate to.

#### Exercise
Find the top 10 movies by Rotten Tomatoes rating with Brad Pitt in it. 
Sort by highest rated.

## Checkpoint 3: Indexes and Aggregations
### **Exercise 7**: Indexes and Query Performance
#### Explanation
To help you better understand the performance of your query, you can view your query's `explain plan`. The explain plan includes a Query Performance Summary with information on the execution of your query such as `execution time`, `number of returned documents`, `number of examined documents`, and `number of examined index keys`.
#### How-to
[Compass GUI explain example](https://www.mongodb.com/docs/compass/current/query-plan)

Shell syntax explain example: `db.movies.find({'tomatoes.viewer.rating':{$gte:3.4}}).explain()`. Of course, `explain()` works with any valid query, not just simple ones like in this example.

[Compass GUI index creation example]()

Shell syntax for create an index: `db.movies.createIndex({<field>': <1|-1})`

As with `sort(<field>': <1|-1})`, `1` means `ASC` and `-1` means `DESC`. If you know you need results sorted in a particular way most of the time, it helps to have a data structure like an index already sorted in the desired manner to reduce latency and hardware resources.

#### Exercise
Create an index on `tomatoes.viewer.rating` (ascending or descending) and re-run the `explain()`. 

You should now see `IXSCAN` (i.e. "index scan"), which means the query will leverage this new index to deliver the same results faster and more effiently. Previously, you should have seen `COLLSCAN` (i.e. "collection scan"), which means every document needed to be examined to fulfill the query. This is inefficient in the same way table scans are inefficient in SQL.

### **Exercise 8**: Aggregations
#### Explanation
Aggregations allow you to compute new data and support complex manipulation of documents such as calculating new/virtual fields, grouping & summarizing values, reshaping documents, migrating data, etc.

Comparing syntax for `find(...)`:
```bash
db.listingsAndReviews.find(
  { "address.country": "Canada" },
  { "host.host_total_listings_count": 1, "host.host_name": 1})
  .sort({"host.host_total_listings_count": -1}).limit(1)
```
vs `aggregate([...])`:
```bash
db.listingsAndReviews.aggregate([ //aggregate() - an array of objects
  {$match: {"address.country": "Canada", "price": { $lt: 200, $gt: 100 }}},
  {$project: {"host.host_total_listings_count": 1, "host.host_name": 1 }},
  {$sort: { "host.host_total_listings_count": -1 }},
  {$limit: 1}])
```
Notice how `aggregate()` works in a manner similar to \*nix piping, with the output of one stage becoming the input to the next stage of the aggregation *pipeline*. This linear approach make MongoDB aggregations much more straightforward to create and reason about, especially when using Compass, which provides sample output results at each stage among other helpful capabilities.

Translating `find()`'s query operators from before to `aggregate()`:
- [match](https://www.mongodb.com/docs/manual/reference/operator/aggregation/match/): Equivalent to `find(...)`.
- [project](https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/): Equivalent to `find({query},{projection})`.
- [sort](https://www.mongodb.com/docs/manual/reference/operator/aggregation/sort/): Equivalent to `find(...).sort(<order>)`.
- [limit](https://www.mongodb.com/docs/manual/reference/operator/aggregation/limit/): Equivalent to `find().limit(<int>)`.
- [skip](https://www.mongodb.com/docs/manual/reference/operator/aggregation/skip/): Equivalent to `find().skip(<int>)`.
- [count](https://www.mongodb.com/docs/manual/reference/operator/aggregation/count/): Equivalent to `find().count(<int>)`.

For Compass GUI users, please refer to [this documentation page](https://www.mongodb.com/docs/compass/current/create-agg-pipeline/) for a quick walkthrough on creating aggregations via GUI.

#### Exercise
Translate the following `find()`-based query to an aggregation:
`db.movies.find(filter, project).sort(sort).limit(limit)`, where 
```bash
let filter = {'cast': 'Brad Pitt'}
```
```bash
let project = {_id: 0, title: 1}
```
```bash
let sort = {'tomatoes.viewer.rating': -1}
```
```bash
let limit = 10
```
## Checkpoint 4: Atlas Search
### **Exercise 9**: Import Data Using Compass GUI
#### Explanation
Within this repo's `data/` folder, you will find a [`wikipedia_tiny.json`](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/data/wikipedia_tiny.json) file containing 5,000 documents. These documents are cleaned wikipedia articles that, among some other metadata, contain the article title, body in plaintext, and a 384-dimension vector representation of plaintext body. Below is a snippet of what the records look like:
![wikipedia file snippet as seen from Compass](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_WikpediaSchema.png)
#### Exercise
Create a new collection with database name `devday` and collection name `wikipedia`. Then, import the `wikipedia_tiny.json` tile into it. 
[Please refer to this guide on how to import data files using the Compass GUI](https://www.mongodb.com/docs/compass/current/import-export/#import-data-into-a-collection)
### **Exercise 10**: Create an Atlas Search Index
#### Explanation
[Atlas Search](https://www.mongodb.com/docs/atlas/atlas-search/) is an embedded full-text search capability in MongoDB Atlas that gives you a seamless, scalable experience for building relevance-based app features. Built on Apache Lucene, Atlas Search eliminates the need to run a separate search system alongside your database.

In short, fulltext search queries typically deliver a wider range of records than regular database queries, and those records are returned sorted by `relevancy`. This means that top answers to those queries are computed to be more meaningful to the user. This is in opposition to database queries, where each record in the result set has equal weight to any other in the result set. 

Moreover, fulltext search also delivers capabilities such as typo tolerance through fuzzy matching, highlighting of result snippets matching the query, and more. Feel free to explore some of the capabilities on [this documentation page](https://www.mongodb.com/atlas/search).
#### Exercise
We will be creating search indexes on top of the new `wikipedia` collection. 
[Follow the guidelines here](https://www.mongodb.com/docs/atlas/atlas-search/tutorial/create-index/) to create a new search index **via the Atlas UI**, keeping all configuration at default. Use the **Visual Editor** to create this index. It will take a couple of minutes for the index to be built. The Atlas UI shows the state of the index as it changes. 
>Note that, for the free-tier M0 cluster, only 3 search indexes can be built.

This default index configuration will capture all indexable fields and make them all available for search. This is called `dynamic indexing`, which is useful for collections within which documents' schemas change. However, this approach typically results in a larger index size. We will see how we can optimize this in the next exercise. 

Once the index is ready, go back to Compass. Select the `wikipedia` collection and go to the `Aggregations` tab like before. Hit `Add Stage` and enter `$search` for the first stage. Compass should provide you with the syntax, which should look something like this:
```
/**
 * index: The name of the Search index.
 * text: Analyzed search, with required fields of query and path, the analyzed field(s) to search.
 * compound: Combines ops.
 * span: Find in text field regions.
 * exists: Test for presence of a field.
 * near: Find near number or date.
 * range: Find in numeric or date range.
 */
{
  index: 'string',
  text: {
    query: 'string',
    path: 'string'
  }
}
```

Play around with search queries, using [this documentation root](https://www.mongodb.com/docs/atlas/atlas-search/searching/) as a guide and the examples below.

[Fuzzy search/typo tolerance](https://www.mongodb.com/docs/atlas/atlas-search/text/):
```
$search = {
  index: '<indexName>',
  text: {
	  query: ‘<queryText>’,
	  path: '<indexedFieldName(s)>',
	  fuzzy: {
  	  maxEdits: 2,
  	  prefixLength: 0
	  }
  }
}
```
[Highlighting](https://www.mongodb.com/docs/atlas/atlas-search/highlighting/):
```
{
  index: '<indexName>',
  text: {
	  query: ‘<queryText>’,
	  path: '<indexedFieldName(s)>',
	  fuzzy: {
  	  maxEdits: 2,
  	  prefixLength: 0
	  }
  },
  highlight: {
	  path: "<indexedFieldName>"
  }
}
```
[Compound search](https://www.mongodb.com/docs/atlas/atlas-search/compound/#definition):
```
{
  index: "<indexName",
  compound: {
    should: {
      text: {
        path: "fullplot",
        query: "werewolves",
        fuzzy: {
          maxEdits: 2,
        },
      },
    },
    mustNot: {
      text: {
        path: "fullplot",
        query: "vampires",
      },
    },
  },
}
```
To see the `relevancy score` and `highlights`, add a subsequent `$project` stage to the pipeline:
```
score: {
    $meta: "searchScore",
  },
  highlights: {
    $meta: "searchHighlights",
  },
```
Here is a full aggregation pipeline that can be run via the embedded shell:
```bash
let pipeline = [
  {
    $search: {
      index: "optimized",
      text: {
        query: "test",
        path: "text",
      },
    },
  },
  {
    $project:
      /**
       * specifications: The fields to
       *   include or exclude.
       */
      {
        title: 1,
        text: 1,
        score: {
          $meta: "searchScore",
        },
        highlights: {
          $meta: "searchHighlights",
        },
      },
  },
]
```
then:
```bash
db.wikipedia.aggregate(pipeline)
```

### **Exercise 11**: Create an *Optimized* Atlas Search Index
#### Explanation
In our case, we only care to search on the `title` and `text` fields of each document in the `wikipedia` collection. Moreover, our users exclusively search in English, so we will want title and text to be indexed by an analyzer intelligent enough to apply English grammar to the information. For example, if I search for the word `dog`, I should get back documents mentioning `dog` or `dogs`. If we were to index the information in French or German, the analyzer should be intelligent to understand gendered words and deal with various accent marks. There is [a wide and interesting world of analyzers](https://www.mongodb.com/docs/atlas/atlas-search/analyzers/) out there that are worth exploring!
#### Exercise
Please follow the instructions below to create a new search, optimized search index:
1. In the **Atlas UI**, go to the **Search** page. There is a link called `Search` on the left-hand panel.
2. Select your cluster and hit the `Go to Atlas Search` button. You should see the search index you previously made here. 
3. Hit the `CREATE INDEX` button in the upper-right-hand side. 
4. Keep `Visual Editor` selected and hit the `Next` button.
5. Set the index name to `optimized` and select the `wikipedia` collection in the `devday` database. Hit `Next`.
6. Click `Refine Your Index`.
7. At the top of the page, for the `Index Analyzer` dropdown, select `lucene.english`.
8. Disable `Dynamic Mapping`. We will specific the fields we want to index this time.
9. Click `Add Field Mapping`. Enter `title` for the first field name and keep everything else the same. Hit `Add`.
10. Repeat step 9 for the `text` field.
11. Scroll down and hit `Save Changes`.
12. Hit `Create Search Index` to create your new `optimized` index.

Since this index is scoped to a subset of the fields, it should build a little faster than the first one. Once it's built and has a status of `ACTIVE` like the first one, notice the size difference between the two indexes. For reference, here is a screenshot of mine:
![optimized vs default index size difference](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Atlas_SearchIndexSizeComparison.png)
### **Exercise 12**: Semantic Search
#### Explanation

#### Exercise

### **Exercise 13**: Semantic Search with Pre-Filter
#### Explanation

#### Exercise
