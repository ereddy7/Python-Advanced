class Car:
    def __init__(self,name,model,color): self.name,self.model,self.color=name,model,color
    def info(self): print(self.name,self.model,self.color)
class Employee:
    def __init__(self,name,no,car): self.name,self.no,self.car=name,no,car
    def info(self): print(self.name,self.no); self.car.info()
Employee("Durga",100,Car("Innova","2.5V","Grey")).info()
