class A:
    def m1(self): print("A")
class B(A): pass
class C(B):
    def m1(self): A.m1(self)
C().m1()
