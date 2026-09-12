class A:
    @staticmethod
    def m1(): print("Parent static")
class B(A):
    @staticmethod
    def m2(): super(B,B).m1()
B.m2()
