class Test:
    def m1(self): print("no arg")
    def m1(self,a): print("one arg")
    def m1(self,a,b): print("two arg")
Test().m1(10,20)
