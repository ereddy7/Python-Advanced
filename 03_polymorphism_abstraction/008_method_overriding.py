class P:
    def marry(self): print("Parent implementation")
class C(P):
    def marry(self): super().marry(); print("Child implementation")
C().marry()
