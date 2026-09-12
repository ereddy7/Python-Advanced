import pickle
class Employee:
    def __init__(self,n): self.name=n
with open("emp.dat","wb") as f: pickle.dump(Employee("Durga"),f)
with open("emp.dat","rb") as f: print(pickle.load(f).name)
