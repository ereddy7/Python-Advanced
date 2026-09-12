import sqlite3
with sqlite3.connect("employees.db") as c:
    q=c.cursor(); q.execute("create table if not exists employees(eno integer primary key,ename text,esal real,eaddr text)"); q.execute("delete from employees"); q.executemany("insert into employees values(?,?,?,?)",[(100,"Durga",1000,"Hyd"),(200,"Ravi",2000,"Mumbai")]); c.commit(); print(q.execute("select * from employees").fetchall())
