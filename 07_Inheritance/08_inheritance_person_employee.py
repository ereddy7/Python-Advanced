class Person:
    def __init__(self,n,a): self.name,self.age=n,a
class Employee(Person):
    def __init__(self,n,a,no,s): super().__init__(n,a); self.no,self.salary=no,s
    def info(self): print(self.name,self.age,self.no,self.salary)
Employee("Durga",48,100,10000).info()
