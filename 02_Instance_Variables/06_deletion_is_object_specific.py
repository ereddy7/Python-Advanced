class Test:
    def __init__(self): self.a,self.b,self.c,self.d=10,20,30,40
t1=Test(); t2=Test(); del t1.a; print(t1.__dict__); print(t2.__dict__)
