# Requires: pip install oracledb
import oracledb
with oracledb.connect(user="YOUR_USER",password="YOUR_PASSWORD",dsn="localhost/XEPDB1") as con:
    print(con.version)
