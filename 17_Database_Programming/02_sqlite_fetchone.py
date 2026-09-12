import sqlite3
with sqlite3.connect(":memory:") as c:
    q=c.cursor(); q.execute("create table t(x)"); q.executemany("insert into t values(?)",[(1,),(2,)]); q.execute("select * from t"); print(q.fetchone()); print(q.fetchone())
