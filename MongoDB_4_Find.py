import pymongo

con = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = con["firstdatabase"]
mycol = mydb["firstcol"]

## In MongoDB we use the find and findOne methods to find data in a collection.
## Just like the SELECT statement is used to find data in a table in a MySQL database.

# x = mycol.find_one()

# find() method gives you the same result as SELECT * in MySQL
##for x in mycol.find():
##    print(x)


# The second parameter of the find() method is an object describing which fields to include in the result
# 1 for showing value, 0 for hiding

##for x in mycol.find({},{"_id":0,"name":1,"address":1}):
##    print(x)

# If you specify a field with the value 0, all other fields get the value 1, and vice versa

for x in mycol.find({},{"address":1,"_id":0}):  # if only 1 attribute is given 1, id will be shown along with that
    print(x)

# Mixed 1 and 0 is not allowed(Except if one of the 2 is "_id").
# And in that also, id cannot be 1 and the other one 0 (Error).
