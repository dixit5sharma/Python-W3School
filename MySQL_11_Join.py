import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="admin",database="mydatabase")
pointer = con.cursor()

##pointer.execute("create table products(id int auto_increment primary key, name varchar(255))")
##pointer.execute("alter table products auto_increment=153")
##cmd = "insert into products (name) values(%s)"
##val = [("Chocolate Heaven",),("Milk Heaven",),("Maggi",)]
##pointer.executemany(cmd,val)
##con.commit()
##
##print(pointer.rowcount,"rows inserted ; ID :",pointer.lastrowid)
##

# INNER JOIN
# pointer.execute("select users.name as user,products.name as favorite from users inner join products on users.fav=products.id")
# You can use JOIN instead of INNER JOIN. They will both give you the same result.

# LEFT JOIN
# pointer.execute("select users.name as user,products.name as favorite from users left join products on users.fav=products.id")

# RIGHT JOIN
pointer.execute("select users.name as user,products.name as favorite from users right join products on users.fav=products.id")


p2 = pointer.fetchall()
for i in p2:
    print(i)
