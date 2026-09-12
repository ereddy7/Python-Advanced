import csv
with open("emp.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["ENO","ENAME","ESAL","EADDR"]); w.writerows([[100,"Durga",1000,"Hyd"],[200,"Ravi",2000,"Mumbai"]])
