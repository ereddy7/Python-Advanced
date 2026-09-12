class Car:
    def __init__(self,n,m,c): self.name,self.model,self.color=n,m,c
    def info(self): print(self.name,self.model,self.color)
class Employee:
    def __init__(self,n,no,car): self.name,self.no,self.car=n,no,car
    def info(self): print(self.name,self.no); self.car.info()
Employee("Durga",10000,Car("Innova","2.5V","Grey")).info()
