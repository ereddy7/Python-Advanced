class Outer:
    class Inner:
        def m1(self): print("inner class method")
Outer().Inner().m1()
