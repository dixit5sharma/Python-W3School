import pymongo

con = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = con["firstdatabase"]
mycol = mydb["firstcol"]

# Query is the first argument of find() function and is equivalent to where statement
##myquery = {"address":"Park Lane 38"}

# Advanced Query
##myquery = {"address":{"$gt":"S"}}   # "address" field starts with the letter "S" or higher (alphabetically)

# Regex Query
myquery = {"address":{"$regex":"^S"}}

for x in mycol.find(myquery,{"name":1,"_id":0}):
    print(x)
