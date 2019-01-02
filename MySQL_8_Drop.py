import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="admin",database="mydatabase")
point = con.cursor()

##cmd = "drop table customer"
cmd = "DROP TABLE IF EXISTS customer"
point.execute(cmd)
