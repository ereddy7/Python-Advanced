class P:
    def marry(self): print("Parent choice")
class C(P):
    def marry(self): super().marry(); print("Child choice")
C().marry()
