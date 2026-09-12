class Test:
    a=10
    def __init__(self): Test.b=20
    def m1(self): Test.c=30
    @classmethod
    def m2(cls): cls.d=40
    @staticmethod
    def m3(): Test.e=50
t=Test(); t.m1(); Test.m2(); Test.m3(); print(Test.__dict__)
