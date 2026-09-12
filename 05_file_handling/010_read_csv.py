import csv
with open("emp.csv",encoding="utf-8") as f:
    for row in csv.reader(f): print(*row,sep="\t")
