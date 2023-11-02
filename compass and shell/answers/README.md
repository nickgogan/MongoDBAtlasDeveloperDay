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
![compass insert exercise example](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/blob/main/compass%20and%20shell/images/Compass_InsertOne.png)

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
![]()