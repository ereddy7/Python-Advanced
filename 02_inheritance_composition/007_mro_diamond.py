class A: pass
class B(A): pass
class C(A): pass
class D(B,C): pass
for cls in (A,B,C,D): print(cls.__name__,cls.mro())
