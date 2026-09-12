class P:
    def m1(self): print("Parent")
class C1(P):
    def m2(self): print("Child1")
class C2(P):
    def m3(self): print("Child2")
C1().m1(); C1().m2(); C2().m1(); C2().m3()
