class Account:
    def __init__(self,name,balance,min_balance): self.name,self.balance,self.min_balance=name,balance,min_balance
    def deposit(self,amount): self.balance+=amount
    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance: self.balance-=amount
        else: print("Insufficient funds")
    def __str__(self): return f"{self.name}: {self.balance}"
class Savings(Account):
    def __init__(self,n,b): super().__init__(n,b,0)
class Current(Account):
    def __init__(self,n,b): super().__init__(n,b,-1000)
a=Savings("Durga",10000); a.deposit(5000); a.withdraw(15000); print(a)
