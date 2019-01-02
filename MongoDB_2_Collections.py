import pymongo

con = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = con["firstdatabase"]

# A collection in MongoDB is the same as a table in SQL databases.
mycol = mydb["firstcol"]

# print(con.list_database_names())    # In MongoDB, a database is not created until it gets content! 

print(mydb.list_collection_names()) # In MongoDB, a collection is not created until it gets content!

# Alternative way
collist = mydb.list_collection_names()
if "firstcol" in collist:
    print("collection found")
else:
    print("Nopes")
