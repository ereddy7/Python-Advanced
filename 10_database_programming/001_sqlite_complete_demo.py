import sqlite3
with sqlite3.connect("employees.db") as con:
    cur=con.cursor(); cur.execute("create table if not exists employees(eno integer primary key, ename text, esal real, eaddr text)")
    cur.execute("delete from employees"); cur.executemany("insert into employees values(?,?,?,?)",[(100,"Durga",1000,"Hyd"),(200,"Ravi",2000,"Mumbai")]); con.commit()
    for row in cur.execute("select * from employees"): print(row)
