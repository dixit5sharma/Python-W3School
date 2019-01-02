import pymongo
from bson.objectid import ObjectId

con = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = con["firstdatabase"]
mycol = mydb["firstcol"]

qwery = {"address":"Valley 345"}
newV = {"$set":{"name":"Updated","address":"Address New"}}
# Update One
##upd_one = mycol.update_one(qwery,newV)
##print(upd_one.modified_count,"documents modified")

# Update Many
upd_many = mycol.update_many(qwery,newV)
print(upd_many.modified_count,"documents modified")

for x in mycol.find():
    print(x)
