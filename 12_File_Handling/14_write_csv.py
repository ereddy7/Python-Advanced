import csv
with open("emp.csv","w",newline="") as f: csv.writer(f).writerows([["ENO","ENAME"],[100,"Durga"],[200,"Ravi"]])
