import mysql.connector

##db = mysql.connector.connect(host="root",username="",password="")
##print(db)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin"
)

print(mydb) # <mysql.connector.connection.MySQLConnection object at 0x02CA27D0>
print(type(mydb))   # <class 'mysql.connector.connection.MySQLConnection'>
