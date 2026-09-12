class Test:
    def __init__(self): self.a,self.b,self.c,self.d=10,20,30,40
    def m1(self): del self.d
t=Test(); print(t.__dict__); t.m1(); del t.c; print(t.__dict__)
