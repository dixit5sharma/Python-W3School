import pymongo
from bson.objectid import ObjectId

con = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = con["firstdatabase"]
mycol = mydb["firstcol"]

mycol.drop()

for x in mycol.find().limit(5):
    print(x)
