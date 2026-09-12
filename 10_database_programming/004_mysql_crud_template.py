# Requires mysql-connector-python and a configured MySQL server.
import mysql.connector
con=mysql.connector.connect(host="localhost",database="durgadb",user="root",password="YOUR_PASSWORD")
cur=con.cursor(); cur.execute("create table if not exists employees(eno int primary key,ename varchar(30),esal double,eaddr varchar(30))")
cur.executemany("insert into employees values(%s,%s,%s,%s)",[(100,"Sachin",1000,"Mumbai"),(200,"Dhoni",2000,"Ranchi")]); con.commit()
cur.execute("select * from employees")
for row in cur.fetchall(): print(row)
cur.close(); con.close()
