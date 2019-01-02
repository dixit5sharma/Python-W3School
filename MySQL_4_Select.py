import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="admin",database="mydatabase")
point = con.cursor()

##point.execute("select name,address from customer")
##point.execute("select id,name from customer where address='Seattle, WDC'")
point.execute("select * from customer where address like '%CA%'")

all = point.fetchall()
##all = point.fetchone()
for i in all:
    print(i)
##    print(type(i))  # tuple
