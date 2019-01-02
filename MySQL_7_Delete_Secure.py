import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="admin",database="mydatabase")
point = con.cursor()

cmd = "delete from customer where address = %s"
val = ("Seattle, WDC",)
point.execute(cmd,val)
con.commit()

print(point.rowcount,"rows deleted")
