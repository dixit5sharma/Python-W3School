import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="admin",database="mydatabase")
point = con.cursor()

point.execute("delete from customer where address='Mountview, CA'")
con.commit()

print(point.rowcount,"rows deleted")
