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

## **Exercise 9**: Import Data Using Compass GUI
![create a new database named devday with a regular collection called wikipedia. Then, import the wikipedia_tiny.json file to the collection](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_ImportWikipediaData.gif)

Once done, you should see 5,000 documents in the `wikipedia` collection with a schema like this:
![screenshot of compass gui showing what a handful of documents look like from the wikipedia_tiny.json file](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_WikpediaSchema.png)

## **Exercise 10**: Create Atlas Search Index and Search
First, create a default Atlas Search index by following along the gif below:
![gif of how to create a fulltext search index via the atlas web ui.](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Atlas_CreateSearchIndex.gif)

It should take only a couple of minutes for this index to be created and reach `ACTIVE` status, meaning that it is searchable. Once ready, try running some `$search` queries.
### Shell
[Fuzzy search example](https://www.mongodb.com/docs/atlas/atlas-search/text/)
```
let search = {$search: {
  index: 'default',
  text: {
	query: ‘<user input>’,
	path: 'fullplot',
	fuzzy: {
  	  maxEdits: 2,
  	  prefixLength: 0
	}
  }
}}
```
```
db.wikipedia.aggregate([search])
```
You can see project in the revelancy scores and/or highlights using `$project` like so:
```
let projection = {$project
  title: 1,
  text: 1,
  score: {
    $meta: "searchScore",
  },
  highlights: {
    $meta: "searchHighlights",
  }}
```
```
db.wikipedia.aggregate([search, projection])
```
This projection can be used with the examples below too.
[Highlighting example](https://www.mongodb.com/docs/atlas/atlas-search/highlighting/)
```
let search = {$search: {
  index: 'default',
  text: {
	query: ‘<user input>’,
	path: 'fullplot',
	fuzzy: {
  	  maxEdits: 2,
  	  prefixLength: 0
	}
  },
  highlight: {
	path: "fullplot"
  }
}}
```
```
db.wikipedia.aggregate([search, projection])
```
[Compound example](https://www.mongodb.com/docs/atlas/atlas-search/compound/#definition)
### Compass

## **Exercise 11**: Create an *Optimized* Atlas Search Index
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

Notice the index size difference between the `default` and `optimized` indexes:
![screenshot of atlas ui showing the optimized index is substantially smaller than the default index](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Atlas_SearchIndexSizeComparison.png)

## **Exercise 12**: Semantic Search
Let's create a search index using the embeddings already available for the `wikipedia` collection's docs. 

1. Back in the **Atlas web UI**, go to the **Search** page. There is a link called `Search` on the left-hand panel.
2. Select your cluster and hit the `Go to Atlas Search` button. You should see the search index you previously made here. 
3. Hit the `CREATE INDEX` button in the upper-right-hand side.
4. This time, select `JSON Editor` and hit `Next`.
5. Name this index `vector` and replace the default definition with this one:
```JSON
{
  "mappings": {
    "dynamic": false,
    "fields": {
      "language": [{
        "type": "token",          
        "normalizer": "lowercase"
        },
        {
          "type": "string"
        }
      ],
      "vector": {
        "dimensions": 384,
        "similarity": "cosine",
        "type": "knnVector"
      }
    }
  }
}
```
6. Select the `devday` database's `wikipedia` collection to build this index on and hit `Next`.
7. Hit `Create Search Index`.

It should take only a couple of minutes for this index to be created and reach `ACTIVE` status, meaning that it is searchable. Once ready, run the vector search query via shell or Compass using the following vector:
```
[0.011573508381843567, 0.025136180222034454, -0.03670182079076767, 0.05932481214404106, -0.007148992270231247, -0.04119409620761871, 0.07708732038736343, 0.037442516535520554, 0.012449102476239204, -0.006117624696344137, 0.017034228891134262, -0.07701531797647476, -0.0003942555340472609, 0.027909113094210625, -0.01598912477493286, -0.06827528774738312, 0.008884701877832413, -0.02028072066605091, -0.08035992830991745, -0.013074136339128017, -0.041099902242422104, -0.025898128747940063, -0.02653864212334156, 0.033052392303943634, -0.022079147398471832, 0.02104610949754715, -0.05792201682925224, 0.03294873610138893, 0.02970735915005207, -0.062248315662145615, 0.03878805413842201, 0.03199061006307602, 0.015330723486840725, 0.0453069768846035, 0.053149424493312836, 0.013360598124563694, 0.041224874556064606, 0.028142929077148438, 0.019398396834731102, -0.00325228413566947, -0.0036123981699347496, -0.1428602933883667, 0.03807120770215988, -0.010916270315647125, 0.026093879714608192, 0.0413699708878994, -0.01601581461727619, 0.053560156375169754, -0.05685950815677643, 0.012246794067323208, -0.03499656170606613, -0.039754077792167664, -0.0461430549621582, -0.03911232948303223, -0.018003594130277634, 0.021634189411997795, -0.006461430341005325, -0.026569517329335213, 0.048728764057159424, 0.0434005968272686, 0.0461999736726284, -0.03447902575135231, -0.024219239130616188, 0.05564909800887108, 0.0246245376765728, 0.019485577940940857, 0.011352903209626675, -0.02576233446598053, -0.032244496047496796, -0.03265222907066345, -0.014595886692404747, 0.014690297655761242, 0.010304473340511322, 0.07407968491315842, 0.08006174117326736, -0.004143617581576109, 0.00271422928199172, -0.07674671709537506, 0.05881533399224281, -0.0048391674645245075, -0.08736331015825272, -0.046462029218673706, -0.039625417441129684, 0.05249401181936264, 0.024801554158329964, 0.08080150187015533, 0.11981362849473953, 0.03177151083946228, -0.11397252231836319, 0.010673915036022663, 0.019723784178495407, 0.03871838375926018, -0.034542348235845566, -0.006243137642741203, -0.04255080223083496, 0.022628607228398323, 0.008293558843433857, -0.019443700090050697, -0.02325102873146534, 0.24533754587173462, 0.0494421161711216, 0.029147367924451828, -0.005753751378506422, -0.020419558510184288, -0.07761149108409882, -0.042979128658771515, 0.000430352461989969, -0.06692603975534439, 0.07076043635606766, 0.0065070209093391895, -0.05844531208276749, -0.005057237576693296, 0.030943823978304863, 0.02757960371673107, 0.027111126109957695, -0.06818623095750809, -0.0657687559723854, 0.059077661484479904, -0.031894147396087646, 0.040606047958135605, 0.05710184574127197, 0.006903495639562607, 0.006207591388374567, -0.013271572068333626, 0.031240442767739296, -0.04029695689678192, 0.07085219770669937, -4.846278151060217e-33, 0.021934309974312782, -0.10270478576421738, 0.056213222444057465, 0.09758369624614716, -0.05268492549657822, 0.01909760572016239, -0.010507515631616116, 0.07035727053880692, -0.009123305790126324, 0.05957060679793358, 0.00933860708028078, -0.015523107722401619, -0.023274024948477745, 0.02397681400179863, 0.10208837687969208, 0.09320352226495743, -0.033136047422885895, 0.011721508577466011, -0.06560060381889343, 0.031464774161577225, -0.023807885125279427, -0.04873918741941452, 0.012257843278348446, -0.04001425951719284, -0.07650823146104813, -0.0355532206594944, -0.0013623012928292155, -0.016429129987955093, 0.016882436349987984, -0.0003748629824258387, -0.0527249313890934, 0.02988101728260517, -0.07291106879711151, 0.06912258267402649, -0.017607856541872025, -0.005510199815034866, 0.012954692356288433, -0.022701852023601532, 0.026741325855255127, -0.02584582194685936, -0.0402020700275898, -0.013495105318725109, 0.0007998105720616877, 0.028601255267858505, 0.03194248303771019, -0.031607117503881454, -0.029549837112426758, -0.020251324400305748, 0.04817793890833855, -0.001307600294239819, -0.013747215270996094, 0.02003014087677002, -0.06870562583208084, -0.021960847079753876, -0.0313321091234684, 0.04928041622042656, 0.012094753794372082, -0.05886812508106232, -0.026465734466910362, 0.0598900131881237, 0.06764866411685944, 0.03401561081409454, -0.05288434773683548, 0.059719402343034744, -0.02548256516456604, -0.02072996273636818, -0.05382559821009636, -0.09741072356700897, 0.047928232699632645, 0.05239959806203842, -0.023259567096829414, -0.06907135248184204, 0.01665687747299671, 0.028476417064666748, -0.029204869642853737, -0.035486698150634766, -0.012644220143556595, 0.07333991676568985, -0.01943499781191349, -0.0632789134979248, 0.09606631845235825, -0.07743873447179794, 0.01593952625989914, -0.04480088874697685, 0.016302691772580147, -0.0007481018546968699, -0.008702695369720459, -0.09881407767534256, 0.0057428390718996525, -0.07192353904247284, -0.032677676528692245, 0.0198945552110672, 0.003859780030325055, -0.02555113658308983, 0.0823836699128151, 4.08626411524599e-33, -0.02948819287121296, 0.02555151656270027, -0.05106087401509285, 0.15531231462955475, 0.05231142044067383, -0.03454818204045296, 0.13314682245254517, -0.019209740683436394, -0.059767063707113266, 0.12289652973413467, 0.01020291168242693, -0.04967312142252922, 0.058467213064432144, 0.012732676230370998, -0.01658635586500168, 0.012795528396964073, 0.045758169144392014, -0.06982148438692093, -0.04852410778403282, -0.004963504150509834, -0.09043655544519424, 0.06992126256227493, 0.009389102458953857, -0.006744624115526676, -0.10609240084886551, 0.03109489008784294, 0.049425847828388214, -0.04487113282084465, -0.007371764630079269, -0.033561088144779205, 0.07605833560228348, 0.007239122409373522, -0.042201463133096695, 0.07079152762889862, 0.047472018748521805, 0.02078300341963768, 0.15331053733825684, -0.0083940289914608, -0.025880761444568634, 0.060799166560173035, 0.06681564450263977, 0.064722940325737, 0.049820322543382645, 0.08878500759601593, -0.03294115141034126, 0.07035744190216064, 0.017195409163832664, -0.030185343697667122, 0.03854382038116455, 0.04846976324915886, -0.06051008775830269, 0.03053232468664646, 0.015603967942297459, -0.030421309173107147, -0.009440446272492409, -0.04105139151215553, -0.06789780408143997, 0.01019960455596447, -0.025656629353761673, 0.021715648472309113, -0.06997868418693542, 0.09247464686632156, -0.035719819366931915, 0.0701378807425499, -0.06342041492462158, -0.03294041380286217, -0.04619632288813591, 0.05414000153541565, 0.05172339454293251, 0.042922209948301315, 0.01347502414137125, 0.016596682369709015, -0.04410717636346817, -0.01972007192671299, 0.03620152175426483, -0.01966143399477005, -0.11567908525466919, 0.00595499761402607, 0.0045669060200452805, -0.04494287446141243, -0.06840218603610992, -0.08530446887016296, -0.0709521472454071, 0.08038382977247238, -0.05798294395208359, 0.057827211916446686, 0.05022648721933365, 0.059423044323921204, -0.03655630350112915, 0.00926964357495308, 0.05252375826239586, 0.027989575639367104, -0.03336919844150543, -0.05078495666384697, -0.012864768505096436, -1.4297850903233211e-08, -0.04052522033452988, -0.08579083532094955, 0.04516823962330818, 0.021677006036043167, -0.022338498383760452, 0.012207704596221447, -0.032489120960235596, -0.01695290580391884, -0.027171028777956963, 0.006002899259328842, 0.0402761772274971, 0.026962704956531525, -0.035624682903289795, 0.07408847659826279, 0.03237416222691536, -0.09056803584098816, -0.031741589307785034, 0.040925294160842896, -0.009956026449799538, 0.030688408762216568, -0.0769139751791954, 0.04158458486199379, 0.00019602153042797, 0.06277656555175781, -0.03609062731266022, 0.04884403944015503, 0.05422690138220787, 0.1266198605298996, -0.003848724765703082, 0.0008294433355331421, 0.06961402297019958, 0.04400506243109703, -0.03208089992403984, -0.08523827791213989, 0.013769851997494698, 0.022801866754889488, -0.0028472745325416327, -0.00678517809137702, 0.03758794814348221, 0.035276927053928375, -0.06678414344787598, 0.021526463329792023, 0.037526607513427734, -0.04542553797364235, -0.051031675189733505, -0.06799469143152237, -0.030867084860801697, -0.03639031946659088, -0.014874979853630066, -0.0936829149723053, -0.03157731890678406, 0.010241780430078506, 0.015077218413352966, -0.0023830991704016924, 0.024135461077094078, -0.01328529603779316, 0.00658379215747118, 0.024441566318273544, -0.13713598251342773, 0.06391417235136032, 0.19671830534934998, -0.006029617041349411, 0.0531940758228302, -0.055225953459739685]
```
### Shell
1. ```
   use devday
   ```
2. ```
   let vector = <aboveVector>
   ```
3. ```
   let agg = [{
   $vectorSearch: {
      queryVector: vector,
      path: ‘vector’,
      numCandidates: 50,
      index: ‘vector’,
      limit: 10,
   }
   }]
   ```
4. ```
   db.wikipedia.aggregate(agg)
   ```
### Compass
![$vectorSearch aggregation via the compass ui](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_SemanticSearch.png)

## **Exercise 13**: Semantic Search with Filter
### Shell
1. ```
   let agg = [{
   $vectorSearch: {
      queryVector: vector,
      Path: ‘vector’,
      numCandidates: 50,
      index: ‘vector’,
      limit: 10,
      filter: {
         $and: [{
         'language': {$eq:'english'}
         }]
      }
   }
   }]
  ```
2. ```
   db.wikipedia.aggregate(agg)
   ```
### Compass
![the same $vectorSearch aggregation as the previous exercise, but augmented with a filter clause to only run semantic search on the english subset of the wikipedia collection. The query uses the language field of the schema.](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_SemanticSearchWithFilter.png)