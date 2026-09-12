class Employee:
    def __init__(self,n,s): self.name,self.salary=n,s
    def display(self): print(self.name,self.salary)
class Test:
    @staticmethod
    def modify(emp): emp.salary+=10000; emp.display()
Test.modify(Employee("Durga",10000))
