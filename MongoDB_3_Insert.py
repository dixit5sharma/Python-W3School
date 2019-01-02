import pymongo

con = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = con["firstdatabase"]
mycol = mydb["firstcol"]

# A document in MongoDB is the same as a record in SQL databases.

# mydict = { "name": "Bianca", "address": "Precezei Metro" }
# inserted = mycol.insert_one(mydict)
# 
# print(inserted.inserted_id)   # 5bf58c9d202fec5b329abb09


# Insert_Many

##mylist = [
##  { "name": "Amy", "address": "Apple st 652"},
##  { "name": "Hannah", "address": "Mountain 21"},
##  { "name": "Michael", "address": "Valley 345"},
##  { "name": "Sandy", "address": "Ocean blvd 2"},
##  { "name": "Betty", "address": "Green Grass 1"},
##  { "name": "Richard", "address": "Sky st 331"},
##  { "name": "Susan", "address": "One way 98"},
##  { "name": "Vicky", "address": "Yellow Garden 2"},
##  { "name": "Ben", "address": "Park Lane 38"},
##  { "name": "William", "address": "Central st 954"},
##  { "name": "Chuck", "address": "Main Road 989"},
##  { "name": "Viola", "address": "Sideway 1633"}
##]
##
##ins = mycol.insert_many(mylist)
##print(ins.inserted_ids) # [ObjectId('5bf59e69202fec579a325142'), ObjectId('5bf59e69202fec579a325143'), ObjectId('5bf59e69202fec579a325144'), ObjectId('5bf59e69202fec579a325145'), ObjectId('5bf59e69202fec579a325146'), ObjectId('5bf59e69202fec579a325147'), ObjectId('5bf59e69202fec579a325148'), ObjectId('5bf59e69202fec579a325149'), ObjectId('5bf59e69202fec579a32514a'), ObjectId('5bf59e69202fec579a32514b'), ObjectId('5bf59e69202fec579a32514c'), ObjectId('5bf59e69202fec579a32514d')]


mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

ins = mycol.insert_many(mylist)
print(ins.inserted_ids)
