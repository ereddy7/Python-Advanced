class Student:
    def __init__(self,name,marks): self.name,self.marks=name,marks
    def display(self): print("Hi",self.name,self.marks)
    def grade(self): print("First" if self.marks>=60 else "Second" if self.marks>=50 else "Third" if self.marks>=35 else "Failed")
Student("Durga",90).display(); Student("Durga",90).grade()
