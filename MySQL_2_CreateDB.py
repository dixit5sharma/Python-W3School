import mysql.connector

data = mysql.connector.connect(host="localhost",user="root",password="admin")

cur = data.cursor()
##print(cur)   # MySQLCursor: (Nothing executed yet)
##print(type(cur)) # <class 'mysql.connector.cursor.MySQLCursor'>

# cur.execute("create database mydatabase")

cur.execute("show databases")

for x in cur:
    print(x)    
##    print(type(x))  # tuple
