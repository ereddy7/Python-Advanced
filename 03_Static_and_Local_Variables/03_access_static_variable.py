class Test:
    a=10
    def __init__(self): print(self.a,Test.a)
    @classmethod
    def cm(cls): print(cls.a,Test.a)
    @staticmethod
    def sm(): print(Test.a)
t=Test(); t.cm(); t.sm()
