import pymongo
from bson.objectid import ObjectId

con = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = con["firstdatabase"]
mycol = mydb["firstcol"]

##If the query finds more than one document, only the first occurrence is deleted
# qwery = {"address":{"$regex":"^S"}}
qwery = {"_id":ObjectId('5bf59e69202fec579a32514b')}
# Delete One
##del_one = mycol.delete_one(qwery)
##print(del_one.deleted_count,"documents deleted")

# Delete Many
del_many = mycol.delete_many(qwery)
print(del_many.deleted_count,"documents deleted")

for x in mycol.find():
    print(x)
