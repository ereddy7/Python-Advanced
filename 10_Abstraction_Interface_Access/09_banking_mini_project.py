class Account:
    def __init__(self,n,b,m): self.name,self.balance,self.minimum=n,b,m
    def deposit(self,a): self.balance+=a
    def withdraw(self,a):
        if self.balance-a>=self.minimum: self.balance-=a
        else: print("Insufficient Funds")
    def __str__(self): return f"{self.name}: {self.balance}"
class Savings(Account):
    def __init__(self,n,b): super().__init__(n,b,0)
a=Savings("Durga",10000); a.deposit(5000); a.withdraw(16000); print(a)
