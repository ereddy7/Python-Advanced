# Configure credentials before running. Requires oracledb.
import oracledb
with oracledb.connect(user="YOUR_USER",password="YOUR_PASSWORD",dsn="localhost/XEPDB1") as con:
    with con.cursor() as cur:
        cur.execute("create table employees(eno number primary key, ename varchar2(30), esal number, eaddr varchar2(30))")
        cur.executemany("insert into employees values(:1,:2,:3,:4)",[(100,"Durga",1000,"Hyd"),(200,"Ravi",2000,"Mumbai")])
        con.commit(); cur.execute("select * from employees")
        for row in cur: print(row)
