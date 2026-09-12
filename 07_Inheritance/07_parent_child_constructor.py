class P:
    def __init__(self): print(id(self))
class C(P): pass
c=C(); print(id(c))
