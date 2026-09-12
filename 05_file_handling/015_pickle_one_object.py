import pickle
class Employee:
    def __init__(self,no,name): self.no,self.name=no,name
    def display(self): print(self.no,self.name)
with open("emp.dat","wb") as f: pickle.dump(Employee(100,"Durga"),f)
with open("emp.dat","rb") as f: pickle.load(f).display()
