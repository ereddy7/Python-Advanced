class Student:
    def __init__(self,n,r): self.name,self.roll=n,r
    def __str__(self): return f"Student {self.name}, {self.roll}"
print(Student("Durga",101))
