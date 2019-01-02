import pymongo

con = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = con["firstdatabase"]
mycol = mydb["firstcol"]

myquery = {"address":{"$regex":"^S"}}

# sort("attribute",1/-1)    1 - ascending, -1 - descending
for x in mycol.find(myquery,{"name":1,"address":1}).sort("name",-1):
    print(x)


##mydoc = mycol.find().sort("name", -1)
##for x in mydoc:
##    print(x)
