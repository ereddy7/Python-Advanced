from abc import ABC,abstractmethod
class I(ABC):
    @abstractmethod
    def m1(self): pass
    @abstractmethod
    def m2(self): pass
class A(I):
    def m1(self): print("m1")
class C(A):
    def m2(self): print("m2")
x=C(); x.m1(); x.m2()
