class Employee:
    def __init__(self,s): self.salary=s
    def __mul__(self,t): return self.salary*t.days
class TimeSheet:
    def __init__(self,d): self.days=d
print(Employee(500)*TimeSheet(25))
