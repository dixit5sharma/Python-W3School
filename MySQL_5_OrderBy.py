import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="admin",database="mydatabase")
point = con.cursor()

##point.execute("select * from customer order by name")
point.execute("select * from customer order by name desc")

p2 = point.fetchall()
# print(type(p2)) # list of tuples
for i in p2:
    print(i)
