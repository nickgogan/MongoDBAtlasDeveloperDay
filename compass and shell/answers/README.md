# Exercise Answers

## **Exercise 1**: Insert operations

Shell: 
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

Compass: 
![compass insert exercise answer](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_InsertOne.png)

## **Exercise 2**: Update operations

Shell:
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

Compass:
![compass update exercise answer](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_UpdateOne.png)

## **Exercise 3**: Delete operations
Shell:
```
db.mycoll.deleteOne({'name.last': 'Bo'})
```

Compass:
![compass delete exercise answer](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_DeleteOne.png)

## **Exercise 4**: Drop a database using the Compass GUI

![compass drop database exercise answer pt 1](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_DropDB1.png)

![compass drop database exercise answer pt 2](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_DropDB2.png)