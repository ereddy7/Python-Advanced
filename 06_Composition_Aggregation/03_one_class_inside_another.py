class X:
    a=10
    def __init__(self): self.b=20
    def m1(self): print("X.m1")
class Y:
    c=30
    def __init__(self): self.d=40
    def m3(self):
        x=X(); print(x.a,x.b); x.m1(); print(Y.c,self.d)
Y().m3()
