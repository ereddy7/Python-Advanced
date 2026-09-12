class A:
    def m1(self): print("A")
class B:
    def m1(self): print("B")
class C: pass
class X(A,B): pass
class Y(B,C): pass
class P(X,Y,C): pass
P().m1(); print(P.mro())
