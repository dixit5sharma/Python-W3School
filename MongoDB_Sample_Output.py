Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pymongo
>>> 
======= RESTART: C:/Python371/MyP_Try/MongoDB_1_Connection_CreateDB.py =======
['admin', 'config', 'local']
>>> 
======= RESTART: C:/Python371/MyP_Try/MongoDB_1_Connection_CreateDB.py =======
Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_1_Connection_CreateDB.py", line 3, in <module>
    myclient = pymongo.MongoClient("mongodb://localhost:27017//")
  File "C:\Python371\lib\site-packages\pymongo\mongo_client.py", line 494, in __init__
    res = uri_parser.parse_uri(entity, port, warn=True)
  File "C:\Python371\lib\site-packages\pymongo\uri_parser.py", line 435, in parse_uri
    raise InvalidURI('Bad database name "%s"' % dbase)
pymongo.errors.InvalidURI: Bad database name "/"
>>> 
======= RESTART: C:/Python371/MyP_Try/MongoDB_1_Connection_CreateDB.py =======
<bound method MongoClient.list_database_names of MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)>
>>> 
======= RESTART: C:/Python371/MyP_Try/MongoDB_1_Connection_CreateDB.py =======
['admin', 'config', 'local']
>>> 
======= RESTART: C:/Python371/MyP_Try/MongoDB_1_Connection_CreateDB.py =======
<class 'list'>
>>> 
======= RESTART: C:/Python371/MyP_Try/MongoDB_1_Connection_CreateDB.py =======
<class 'pymongo.mongo_client.MongoClient'>
['admin', 'config', 'local']
>>> 
======= RESTART: C:/Python371/MyP_Try/MongoDB_1_Connection_CreateDB.py =======
<class 'pymongo.database.Database'>
['admin', 'config', 'local']
>>> 
======= RESTART: C:/Python371/MyP_Try/MongoDB_1_Connection_CreateDB.py =======
Nopes
>>> 
=========== RESTART: C:/Python371/MyP_Try/MongoDB_2_Collections.py ===========
['admin', 'config', 'local']
>>> 
=========== RESTART: C:/Python371/MyP_Try/MongoDB_2_Collections.py ===========
['admin', 'config', 'local']
[]
>>> 
=========== RESTART: C:/Python371/MyP_Try/MongoDB_2_Collections.py ===========
['admin', 'config', 'local']
[]
>>> 
=========== RESTART: C:/Python371/MyP_Try/MongoDB_2_Collections.py ===========
['admin', 'config', 'local']
[]
Nopes
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_3_Insert.py =============
5bf58c9d202fec5b329abb09
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_3_Insert.py =============
[ObjectId('5bf59e69202fec579a325142'), ObjectId('5bf59e69202fec579a325143'), ObjectId('5bf59e69202fec579a325144'), ObjectId('5bf59e69202fec579a325145'), ObjectId('5bf59e69202fec579a325146'), ObjectId('5bf59e69202fec579a325147'), ObjectId('5bf59e69202fec579a325148'), ObjectId('5bf59e69202fec579a325149'), ObjectId('5bf59e69202fec579a32514a'), ObjectId('5bf59e69202fec579a32514b'), ObjectId('5bf59e69202fec579a32514c'), ObjectId('5bf59e69202fec579a32514d')]
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_3_Insert.py =============
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_4_Find.py ==============
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_4_Find.py ==============
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_4_Find.py ==============
{'name': 'Bianca', 'address': 'Precezei Metro'}
{'name': 'Amy', 'address': 'Apple st 652'}
{'name': 'Hannah', 'address': 'Mountain 21'}
{'name': 'Michael', 'address': 'Valley 345'}
{'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'name': 'Betty', 'address': 'Green Grass 1'}
{'name': 'Richard', 'address': 'Sky st 331'}
{'name': 'Susan', 'address': 'One way 98'}
{'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'name': 'Ben', 'address': 'Park Lane 38'}
{'name': 'William', 'address': 'Central st 954'}
{'name': 'Chuck', 'address': 'Main Road 989'}
{'name': 'Viola', 'address': 'Sideway 1633'}
{'name': 'John', 'address': 'Highway 37'}
{'name': 'Peter', 'address': 'Lowstreet 27'}
{'name': 'Amy', 'address': 'Apple st 652'}
{'name': 'Hannah', 'address': 'Mountain 21'}
{'name': 'Michael', 'address': 'Valley 345'}
{'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'name': 'Betty', 'address': 'Green Grass 1'}
{'name': 'Richard', 'address': 'Sky st 331'}
{'name': 'Susan', 'address': 'One way 98'}
{'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'name': 'Ben', 'address': 'Park Lane 38'}
{'name': 'William', 'address': 'Central st 954'}
{'name': 'Chuck', 'address': 'Main Road 989'}
{'name': 'Viola', 'address': 'Sideway 1633'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_4_Find.py ==============
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola'}
{'_id': 1, 'name': 'John'}
{'_id': 2, 'name': 'Peter'}
{'_id': 3, 'name': 'Amy'}
{'_id': 4, 'name': 'Hannah'}
{'_id': 5, 'name': 'Michael'}
{'_id': 6, 'name': 'Sandy'}
{'_id': 7, 'name': 'Betty'}
{'_id': 8, 'name': 'Richard'}
{'_id': 9, 'name': 'Susan'}
{'_id': 10, 'name': 'Vicky'}
{'_id': 11, 'name': 'Ben'}
{'_id': 12, 'name': 'William'}
{'_id': 13, 'name': 'Chuck'}
{'_id': 14, 'name': 'Viola'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_4_Find.py ==============
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'address': 'Mountain 21'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'address': 'Sky st 331'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'address': 'Main Road 989'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'address': 'Sideway 1633'}
{'_id': 1, 'address': 'Highway 37'}
{'_id': 2, 'address': 'Lowstreet 27'}
{'_id': 3, 'address': 'Apple st 652'}
{'_id': 4, 'address': 'Mountain 21'}
{'_id': 5, 'address': 'Valley 345'}
{'_id': 6, 'address': 'Ocean blvd 2'}
{'_id': 7, 'address': 'Green Grass 1'}
{'_id': 8, 'address': 'Sky st 331'}
{'_id': 9, 'address': 'One way 98'}
{'_id': 10, 'address': 'Yellow Garden 2'}
{'_id': 11, 'address': 'Park Lane 38'}
{'_id': 12, 'address': 'Central st 954'}
{'_id': 13, 'address': 'Main Road 989'}
{'_id': 14, 'address': 'Sideway 1633'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_4_Find.py ==============
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola'}
{'_id': 1, 'name': 'John'}
{'_id': 2, 'name': 'Peter'}
{'_id': 3, 'name': 'Amy'}
{'_id': 4, 'name': 'Hannah'}
{'_id': 5, 'name': 'Michael'}
{'_id': 6, 'name': 'Sandy'}
{'_id': 7, 'name': 'Betty'}
{'_id': 8, 'name': 'Richard'}
{'_id': 9, 'name': 'Susan'}
{'_id': 10, 'name': 'Vicky'}
{'_id': 11, 'name': 'Ben'}
{'_id': 12, 'name': 'William'}
{'_id': 13, 'name': 'Chuck'}
{'_id': 14, 'name': 'Viola'}
	
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_4_Find.py ==============
Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_4_Find.py", line 25, in <module>
    for x in mycol.find({},{"address":0,"name":1}):  # if only 1 attribute is given 1, id will be shown along with that
  File "C:\Python371\lib\site-packages\pymongo\cursor.py", line 1189, in next
    if len(self.__data) or self._refresh():
  File "C:\Python371\lib\site-packages\pymongo\cursor.py", line 1104, in _refresh
    self.__send_message(q)
  File "C:\Python371\lib\site-packages\pymongo\cursor.py", line 982, in __send_message
    helpers._check_command_response(first)
  File "C:\Python371\lib\site-packages\pymongo\helpers.py", line 155, in _check_command_response
    raise OperationFailure(msg % errmsg, code, response)
pymongo.errors.OperationFailure: Projection cannot have a mix of inclusion and exclusion.
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_4_Find.py ==============
Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_4_Find.py", line 25, in <module>
    for x in mycol.find({},{"address":0,"_id":1}):  # if only 1 attribute is given 1, id will be shown along with that
  File "C:\Python371\lib\site-packages\pymongo\cursor.py", line 1189, in next
    if len(self.__data) or self._refresh():
  File "C:\Python371\lib\site-packages\pymongo\cursor.py", line 1104, in _refresh
    self.__send_message(q)
  File "C:\Python371\lib\site-packages\pymongo\cursor.py", line 982, in __send_message
    helpers._check_command_response(first)
  File "C:\Python371\lib\site-packages\pymongo\helpers.py", line 155, in _check_command_response
    raise OperationFailure(msg % errmsg, code, response)
pymongo.errors.OperationFailure: Projection cannot have a mix of inclusion and exclusion.
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_4_Find.py ==============
{'address': 'Precezei Metro'}
{'address': 'Apple st 652'}
{'address': 'Mountain 21'}
{'address': 'Valley 345'}
{'address': 'Ocean blvd 2'}
{'address': 'Green Grass 1'}
{'address': 'Sky st 331'}
{'address': 'One way 98'}
{'address': 'Yellow Garden 2'}
{'address': 'Park Lane 38'}
{'address': 'Central st 954'}
{'address': 'Main Road 989'}
{'address': 'Sideway 1633'}
{'address': 'Highway 37'}
{'address': 'Lowstreet 27'}
{'address': 'Apple st 652'}
{'address': 'Mountain 21'}
{'address': 'Valley 345'}
{'address': 'Ocean blvd 2'}
{'address': 'Green Grass 1'}
{'address': 'Sky st 331'}
{'address': 'One way 98'}
{'address': 'Yellow Garden 2'}
{'address': 'Park Lane 38'}
{'address': 'Central st 954'}
{'address': 'Main Road 989'}
{'address': 'Sideway 1633'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_5_Query.py ==============
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_5_Query.py ==============
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben'}
{'_id': 11, 'name': 'Ben'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_5_Query.py ==============
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola'}
{'_id': 5, 'name': 'Michael'}
{'_id': 8, 'name': 'Richard'}
{'_id': 10, 'name': 'Vicky'}
{'_id': 14, 'name': 'Viola'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_5_Query.py ==============
Michael
Richard
Vicky
Viola
Michael
Richard
Vicky
Viola
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_5_Query.py ==============
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola'}
{'_id': 5, 'name': 'Michael'}
{'_id': 8, 'name': 'Richard'}
{'_id': 10, 'name': 'Vicky'}
{'_id': 14, 'name': 'Viola'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_5_Query.py ==============
{'name': 'Michael'}
{'name': 'Richard'}
{'name': 'Vicky'}
{'name': 'Viola'}
{'name': 'Michael'}
{'name': 'Richard'}
{'name': 'Vicky'}
{'name': 'Viola'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_5_Query.py ==============
{'name': 'Richard'}
{'name': 'Viola'}
{'name': 'Richard'}
{'name': 'Viola'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_5_Query.py ==============
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_6_Sort.py ==============
Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_6_Sort.py", line 9, in <module>
    for x in mycol.find(myquery,{"name":1,"address":1}).sort(name):
NameError: name 'name' is not defined
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_6_Sort.py ==============
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_6_Sort.py ==============
Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_6_Sort.py", line 9, in <module>
    for x in mycol.find(myquery,{"name":1,"address":0}).sort("name"):
  File "C:\Python371\lib\site-packages\pymongo\cursor.py", line 1189, in next
    if len(self.__data) or self._refresh():
  File "C:\Python371\lib\site-packages\pymongo\cursor.py", line 1104, in _refresh
    self.__send_message(q)
  File "C:\Python371\lib\site-packages\pymongo\cursor.py", line 982, in __send_message
    helpers._check_command_response(first)
  File "C:\Python371\lib\site-packages\pymongo\helpers.py", line 155, in _check_command_response
    raise OperationFailure(msg % errmsg, code, response)
pymongo.errors.OperationFailure: Projection cannot have a mix of inclusion and exclusion.
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_6_Sort.py ==============
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard'}
{'_id': 8, 'name': 'Richard'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola'}
{'_id': 14, 'name': 'Viola'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_6_Sort.py ==============
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola'}
{'_id': 14, 'name': 'Viola'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard'}
{'_id': 8, 'name': 'Richard'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_6_Sort.py ==============
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_6_Sort.py ==============
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_6_Sort.py ==============
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_7_Delete.py", line 3, in <module>
    con = pymongo.MongoClient("monogodb://localhost:27017/")
  File "C:\Python371\lib\site-packages\pymongo\mongo_client.py", line 494, in __init__
    res = uri_parser.parse_uri(entity, port, warn=True)
  File "C:\Python371\lib\site-packages\pymongo\uri_parser.py", line 357, in parse_uri
    "begin with '%s' or '%s'" % (SCHEME, SRV_SCHEME))
pymongo.errors.InvalidURI: Invalid URI scheme: URI must begin with 'mongodb://' or 'mongodb+srv://'
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
0 documents deleted
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
1 documents deleted
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_7_Delete.py", line 9, in <module>
    del_one = mycol.delete_one(qwery)
  File "C:\Python371\lib\site-packages\pymongo\collection.py", line 1191, in delete_one
    collation=collation, session=session),
  File "C:\Python371\lib\site-packages\pymongo\collection.py", line 1154, in _delete_retryable
    _delete, session)
  File "C:\Python371\lib\site-packages\pymongo\mongo_client.py", line 1248, in _retryable_write
    return self._retry_with_session(retryable, func, s, None)
  File "C:\Python371\lib\site-packages\pymongo\mongo_client.py", line 1201, in _retry_with_session
    return func(session, sock_info, retryable)
  File "C:\Python371\lib\site-packages\pymongo\collection.py", line 1150, in _delete
    retryable_write=retryable_write)
  File "C:\Python371\lib\site-packages\pymongo\collection.py", line 1136, in _delete
    retryable_write=retryable_write)
  File "C:\Python371\lib\site-packages\pymongo\pool.py", line 584, in command
    self._raise_connection_failure(error)
  File "C:\Python371\lib\site-packages\pymongo\pool.py", line 745, in _raise_connection_failure
    raise error
  File "C:\Python371\lib\site-packages\pymongo\pool.py", line 579, in command
    unacknowledged=unacknowledged)
  File "C:\Python371\lib\site-packages\pymongo\network.py", line 114, in command
    codec_options, ctx=compression_ctx)
  File "C:\Python371\lib\site-packages\pymongo\message.py", line 679, in _op_msg
    flags, command, identifier, docs, check_keys, opts)
bson.errors.InvalidDocument: documents must have only string keys, key was <class 'str'>
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
0 documents deleted
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
0 documents deleted
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_7_Delete.py", line 8, in <module>
    qwery = {"_id":{"$gt":ObjectId('5bf59e69202fec579a325145')}}
NameError: name 'ObjectId' is not defined
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_7_Delete.py", line 8, in <module>
    qwery = {"_id":ObjectId('5bf59e69202fec579a325145')}
NameError: name 'ObjectId' is not defined
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
0 documents deleted
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
0 documents deleted
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
0 documents deleted
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325147'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
1 documents deleted
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': ObjectId('5bf59e69202fec579a32514d'), 'name': 'Viola', 'address': 'Sideway 1633'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
2 documents deleted
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325143'), 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
1 documents deleted
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a325149'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
Traceback (most recent call last):
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 217, in __validate
    self.__id = bytes_from_hex(oid)
  File "C:\Python371\lib\site-packages\bson\py3compat.py", line 45, in bytes_from_hex
    return bytes.fromhex(h)
ValueError: non-hexadecimal number found in fromhex() arg at position 23

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_7_Delete.py", line 10, in <module>
    qwery = {"_id":{"$regex":ObjectId('5bf59e69202fec579a32514*')}}
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 125, in __init__
    self.__validate(oid)
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 219, in __validate
    _raise_invalid_id(oid)
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 67, in _raise_invalid_id
    " or a 24-character hex string" % oid)
bson.errors.InvalidId: '5bf59e69202fec579a32514*' is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
Traceback (most recent call last):
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 217, in __validate
    self.__id = bytes_from_hex(oid)
  File "C:\Python371\lib\site-packages\bson\py3compat.py", line 45, in bytes_from_hex
    return bytes.fromhex(h)
ValueError: non-hexadecimal number found in fromhex() arg at position 23

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_7_Delete.py", line 10, in <module>
    qwery = {"_id":ObjectId('5bf59e69202fec579a32514*')}
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 125, in __init__
    self.__validate(oid)
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 219, in __validate
    _raise_invalid_id(oid)
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 67, in _raise_invalid_id
    " or a 24-character hex string" % oid)
bson.errors.InvalidId: '5bf59e69202fec579a32514*' is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
1 documents deleted
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514b'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_7_Delete.py", line 10, in <module>
    qwery = {"_id":ObjectId({"$regex":"5bf59e69202fec579a3251.*"})}
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 125, in __init__
    self.__validate(oid)
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 224, in __validate
    "not %s" % (text_type.__name__, type(oid)))
TypeError: id must be an instance of (bytes, str, ObjectId), not <class 'dict'>
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
Traceback (most recent call last):
  File "C:/Python371/MyP_Try/MongoDB_7_Delete.py", line 10, in <module>
    qwery = {"_id":ObjectId('5bf59e69202fec579a3251')}
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 125, in __init__
    self.__validate(oid)
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 221, in __validate
    _raise_invalid_id(oid)
  File "C:\Python371\lib\site-packages\bson\objectid.py", line 67, in _raise_invalid_id
    " or a 24-character hex string" % oid)
bson.errors.InvalidId: '5bf59e69202fec579a3251' is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_7_Delete.py =============
1 documents deleted
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_8_Update.py =============
1 documents modified
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Updated', 'address': 'Address New'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============= RESTART: C:/Python371/MyP_Try/MongoDB_8_Update.py =============
1 documents modified
0 documents modified
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Updated', 'address': 'Address New'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('5bf59e69202fec579a325148'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('5bf59e69202fec579a32514a'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('5bf59e69202fec579a32514c'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Updated', 'address': 'Address New'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_9_Limit.py ==============
{'_id': ObjectId('5bf58c9d202fec5b329abb09'), 'name': 'Bianca', 'address': 'Precezei Metro'}
{'_id': ObjectId('5bf59e69202fec579a325142'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('5bf59e69202fec579a325144'), 'name': 'Updated', 'address': 'Address New'}
{'_id': ObjectId('5bf59e69202fec579a325145'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('5bf59e69202fec579a325146'), 'name': 'Betty', 'address': 'Green Grass 1'}
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_10_Drop.py ==============
None
>>> 
============== RESTART: C:/Python371/MyP_Try/MongoDB_10_Drop.py ==============
>>> 
