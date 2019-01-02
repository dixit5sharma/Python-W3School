import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")    # <class 'pymongo.mongo_client.MongoClient'>
new = myclient["mydatabase"]    # <class 'pymongo.database.Database'>

# print(myclient.list_database_names())   # <class 'list'>

dblist = myclient.list_database_names()

if "mydatabase" in dblist:
    print("exists")
else:
    print("Nopes")
