class Student:
    def __init__(self,x,y,z): self.name,self.rollno,self.marks=x,y,z
    def display(self): print(f"Student Name:{self.name}\nRollno:{self.rollno}\nMarks:{self.marks}")
Student("Durga",101,80).display(); Student("Sunny",102,100).display()
