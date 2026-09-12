class Person:
    def __init__(self,n,a): self.name,self.age=n,a
    def display(self): print(self.name,self.age)
class Student(Person):
    def __init__(self,n,a,r,m): super().__init__(n,a); self.roll,self.marks=r,m
    def display(self): super().display(); print(self.roll,self.marks)
Student("Durga",22,101,90).display()
