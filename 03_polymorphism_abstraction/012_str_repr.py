class Student:
    def __init__(self,name,roll): self.name,self.roll=name,roll
    def __str__(self): return f"Student(name={self.name}, roll={self.roll})"
    def __repr__(self): return f"Student({self.name!r}, {self.roll!r})"
s=Student("Durga",101); print(str(s)); print(repr(s))
