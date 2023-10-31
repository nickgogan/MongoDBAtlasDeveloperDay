# Compass (& Mongo Shell)

The following is a plaintext version of the exercises in the PDF presentations. It is meant to guide workshop participants through the process by providing code snippets that can be easily copy/pasted into the [MongoDB Compass GUI](https://www.mongodb.com/docs/compass/current/) and its embedded [MongoDB shell (mongosh)](https://www.mongodb.com/docs/mongodb-shell/).

Please also refer to [the PDF of the presentation](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/DevDayPresentation_Full.pdf) to see helpful screenshots to aid in completing the exercises. Answers for both the Compass GUI approach and shell approach are in the PDF. For slides originally containing GIFs, this README will provide either plaintext explanations and/or links to tutorials that walk through exactly the same process as what was captured in the GIF. 

## Checkpoint 0: Prerequisites
1. As a workshop attendee/participants, please ensure that you have followed all of the [list of prerequisites](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/tree/main#prerequisites). Then, please [install MongoDB Compass](https://www.mongodb.com/try/download/compass) and copy this repository to have access to the `wikipedia_tiny.json` file in `data/`.

## Checkpoint 1: CRUD Operations in MongoDB

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

### Exercise 3: Delete operations
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

### Exercise 4
Now, drop (i.e. delete) `mydb` using the [Compass GUI](https://www.mongodb.com/docs/compass/current/databases/#drop-a-database).


### Exercise 5: Read operations (i.e. queries)

Before proceeding to the exercise, switch to using the `sample_mflix` database's `movies` collection. If following using the shell, use the `use` keyword ([Reference](https://www.mongodb.com/docs/compass/current/embedded-shell/#use-the-embedded-mongodb-shell)).
> Notice how the Compass shell provides suggestions (i.e. intellisense)!




