import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="admin",database="mydatabase")
point = con.cursor()

##point.execute("select * from customer limit 2")
point.execute("select * from customer limit 2 offset 1")

p2 = point.fetchall()
for i in p2:
    print(i)
