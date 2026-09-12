from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def wheels(self): pass
class Bus(Vehicle):
    def wheels(self): return 7
class Auto(Vehicle):
    def wheels(self): return 3
print(Bus().wheels(),Auto().wheels())
