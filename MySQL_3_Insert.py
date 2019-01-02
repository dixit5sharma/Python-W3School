import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="admin",database="mydatabase")
point = con.cursor()

# point.execute("create table customer(name varchar(255), address varchar(255))")
# point.execute("alter table customer add column id int auto_increment primary key")

cmd = "insert into customer (name,address) values(%s,%s)"
val = [("Amazon","Seattle, WDC"),("Google","Mountview, CA"),("Apple","Cupertino, CA")]
point.executemany(cmd,val)
con.commit()

print(point.rowcount,"rows inserted ; ID :",point.lastrowid)

##point.execute("show tables")
##for x in point:
##    print(x)
