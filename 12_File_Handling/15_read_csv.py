import csv
open("emp.csv","w").write("ENO,ENAME\n100,Durga\n")
with open("emp.csv") as f:
    for row in csv.reader(f): print(row)
