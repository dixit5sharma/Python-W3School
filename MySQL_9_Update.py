import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="admin",database="mydatabase")
point = con.cursor()

point.execute("update users set fav='155' where name='Apple'")
con.commit()

print(point.rowcount,"row(s) affected")
