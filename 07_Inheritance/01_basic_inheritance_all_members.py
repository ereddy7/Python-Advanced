class P:
    a=10
    def __init__(self): self.b=10
    def m1(self): print("instance")
    @classmethod
    def m2(cls): print("class")
    @staticmethod
    def m3(): print("static")
class C(P): pass
c=C(); print(c.a,c.b); c.m1(); c.m2(); c.m3()
