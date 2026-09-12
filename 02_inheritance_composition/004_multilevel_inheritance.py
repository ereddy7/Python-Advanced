class P:
    def m1(self): print("Parent")
class C(P):
    def m2(self): print("Child")
class CC(C):
    def m3(self): print("Sub child")
x=CC(); x.m1(); x.m2(); x.m3()
