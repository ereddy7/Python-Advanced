class P1:
    def m1(self): print("Parent1")
class P2:
    def m1(self): print("Parent2")
class C(P1,P2): pass
C().m1()
