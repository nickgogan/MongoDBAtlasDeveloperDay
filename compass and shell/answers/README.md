# Exercise Answers

## **Exercise 1**: Insert operations
### Shell
```
db.mycoll.insertOne({
    "name" : {
      "first" : "John",
      "last" : "Doe" },
    "address" : [
      { "location" : "work",
        "address" : {
          "street" : "16 Hatfields",
          "city" : "London",
          "postal_code" : "SE1 8DJ"},
        "geo" : { "type" : "Point", "coord" : [-0.109081, 51.5065752]}
      }
  ],
  "dob" :"1977-04-01T05:00:00Z",
  "retirement_fund" : 1292815.75
})
```
### Compass
![compass insert exercise answer](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_InsertOne.png)

## **Exercise 2**: Update operations
### Shell
```
let newAddress = { 
  "location" : "home",
  "address" : {
    "street" : "123 ABC Street",
    "city" : "AAA",
    "postal_code" : "111111"
  }
}
```
```
db.mycoll.updateOne({'name.last': 'Doe'},{$set: {'name.last': 'Bo'},$push: {'address': newAddress}})
```
### Compass
![compass update exercise answer](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_UpdateOne.png)

## **Exercise 3**: Delete operations
### Shell
```
db.mycoll.deleteOne({'name.last': 'Bo'})
```
### Compass
![compass delete exercise answer](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_DeleteOne.png)

## **Exercise 4**: Drop a database using the Compass GUI

![compass drop database exercise answer pt 1](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_DropDB1.png)

![compass drop database exercise answer pt 2](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_DropDB2.png)

## **Exercise 5**: Read operations (i.e. queries)
### Shell
1. ```
   db.movies.find({title: “Regeneration”})
   ```
2. ```
   db.movies.find({year:1991, cast:'Brad Pitt'})
   ```
3. ```
   db.movies.find({year: {$gt: 1991}})
   ```
4. ```
   db.movies.find({runtime: {$exists: false}})
   ```
5. ```
   db.movies.find({'tomatoes.viewer.rating':{$gte:3.4}})
   ```
### Compass
Copy the shell queries' `{filter}` and pass them into the `Filter` bar near the top, as exemplified below. For example, the `{filter}` portion of this shell `db.movies.find({title: “Regeneration”})` is `{title: “Regeneration”}`:
![compass basic read exercise how-to. Use the shell answers to get the queries and place them where indicated in this gif](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_BasicFind.gif)

## **Exercise 6**: Sort, Limit, Skip, Project
### Shell
1. ```
   let filter = {'cast': 'Brad Pitt'}
   ```
2. ```
   let project = {'cast': 'Brad Pitt'}
   ```
3. ```
   let sort = {'tomatoes.viewer.rating': -1}
   ```
4. ```
   let limit = 10
   ```
5. ```
   db.movies.find(filter, project).sort(sort).limit(10)
   ```

### Compass
1. First, open the `Options` for the `Filter` bar like so:
![compass filter options to set parameters like skip, limit, sort, projection, etc via the compass GUI](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_QueryOptions.png)
2. Then, fill the fields like so:
![compass advanced query exercise answer](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_AdvancedQuery.png)

## **Exercise 7**: Indexes and Query Performance
### Shell
1. ```db.movies.find({'tomatoes.viewer.rating':{$gte:3.4}}).explain()```
2. ```db.movies.createIndex({'tomatoes.viewer.rating': 1})```
3. ```db.movies.find({'tomatoes.viewer.rating':{$gte:3.4}}).explain()```

Notice how, in the second run of `explain()`, MongoDB shows that it will leverage the new index to fulfill the query. 

### Compass
1. First, review how to use the Compass GUI to examine a given query:
![how to examine a query for performance via the compass ui. it shows that mongodb is doing a collection scan, i.e. COLLSCAN, which is analagous to a table scane in the SQL world. It's not something you typically want to see.](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_ExamineQueryBeforeIndex.gif)
1. Next, create an index:
![how to create an index using the compass ui](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_CreateIndex.gif)
1. Finally, re-examine the same query and see the difference. It should look something like this:
![the explain should now show mongodb doing an index scan, i.e. IXSCAN, followed by a fetch, which are much faster and more resource-efficient than scanning all documents as in the collection scan before.](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_ExamineQueryAfterIndex.gif)

## **Exercise 8**: Indexes and Query Performance
### Shell
1. ```
   let pipeline = [
     {$match: { ‘cast’: "Brad Pitt",}},
     {$project: { _id: 0, title: 1}},
     {$sort: { "tomatoes.viewer.rating": -1}},
     {$limit: 10}]
   ```

2. ```
   db.movies.aggregate(pipeline)
   ```
### Compass
1. First, go to the Aggregation builder:
![how to get to the aggregation builder in the compass ui](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_AggBuilder.png)
2. Then, start adding the pipeline stages like so:
![The first stage is $match with a single filter criterion on the cast field that looks like {'cast':'Brad Pitt}. What's cool about this is that the cast field is an array, but we can query it like any other field.](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_AdvancedFind1.png)
![the next stage is $project where we set _id:0 to remove it and title:1. This means that we only see titles. The next stage is $sort, where we sort by rotten tomatoes ratings in descending order. Notice how we can use dot-notation to access nested fields.](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_AdvancedFind2.png)
![the last stage is $limit, with a value of 10](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_AdvancedFind3.png)

BONUS: You can use Compass to craft aggregations and then [export them to either shell syntax or the programming language of your choise](https://www.mongodb.com/docs/compass/current/agg-pipeline-builder/export-pipeline-results/): 
![export aggregations to either shell syntax or a supported programming language](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_AggExport.png)

## **Exercise 9**: 