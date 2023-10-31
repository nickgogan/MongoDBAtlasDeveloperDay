# Compass (& Mongo Shell)

The following is a plaintext version of the exercises in the PDF presentations. It is meant to guide workshop participants through the process by providing code snippets that can be easily copy/pasted into the [MongoDB Compass GUI](https://www.mongodb.com/docs/compass/current/) and its embedded [MongoDB shell (mongosh)](https://www.mongodb.com/docs/mongodb-shell/).

Please also refer to [the PDF of the presentation](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/DevDayPresentation_Full.pdf) to see helpful screenshots to aid in completing the exercises. For slides originally containing GIFs, this README will provide either plaintext explanations and/or links to tutorials that walk through exactly the same process as what was captured in the GIF. 

## Checkpoint 0: Prerequisites
1. As a workshop attendee/participants, please ensure that you have followed all of the [list of prerequisites](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/tree/main#prerequisites). Then, please [install MongoDB Compass](https://www.mongodb.com/try/download/compass) and copy this repository to have access to the `wikipedia_tiny.json` file in `data/`.

## Checkpoint 1: CRUD Operations in MongoDB

1. Via the Atlas web GUI, [load up the sample dataset](https://www.mongodb.com/docs/atlas/sample-data/).


2. [Get your Atlas cluster's connection string](https://www.mongodb.com/docs/guides/atlas/connection-string/) and [connect to it using Compass](https://www.mongodb.com/docs/atlas/compass-connection/).


3. Use Compass to [create a database named `mydb` and collection named `mycoll`](https://www.mongodb.com/docs/compass/current/databases/#create-a-database) (equivalent to a table in SQL) in your Atlas cluster. No need to specify any collection properties. The first set of exercises will be done in this collection. 

Most of the remaining exercises can be completed via either the Compass GUI or via [the embedded MongoDB shell](https://www.mongodb.com/docs/compass/current/embedded-shell/#open-the-embedded-mongodb-shell).

4. **Exercise 1**: Insert the following document into `mycoll`:
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
[Example via Compass GUI](https://www.mongodb.com/docs/compass/current/documents/insert/)

Shell syntax:
```db.<collectionName>.insertOne({key:value},{options})```

```db.<collectionName>.insertMany([{k:v},{k:v}],{options})```






