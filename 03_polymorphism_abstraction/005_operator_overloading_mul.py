class Employee:
    def __init__(self,salary): self.salary=salary
    def __mul__(self,other): return self.salary*other.days
class TimeSheet:
    def __init__(self,days): self.days=days
print(Employee(500)*TimeSheet(25))
