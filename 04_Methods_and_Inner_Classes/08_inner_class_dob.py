class Person:
    def __init__(self): self.name="Durga"; self.db=self.Dob()
    class Dob:
        def display(self): print("Dob=10/5/1947")
p=Person(); print(p.name); p.db.display()
