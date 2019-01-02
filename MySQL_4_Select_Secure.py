import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="admin",database="mydatabase")
point = con.cursor()

cmd = "select * from customer where address =%s"    # When query values are provided by the user, you should escape the values.
val = ("Mountview, CA",)    

point.execute(cmd,val)
fetch = point.fetchall()

for x in fetch:
    print(x)
