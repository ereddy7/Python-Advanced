from abc import ABC,abstractmethod
class Test(ABC):
    @abstractmethod
    def m1(self): pass
print(Test.__abstractmethods__)
