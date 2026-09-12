class Car:
    def info(self): print("Car info")
class Person:
    def eat(self): print("Eating")
class Employee(Person):
    def __init__(self,car): self.car=car
    def info(self): self.eat(); self.car.info()
Employee(Car()).info()
