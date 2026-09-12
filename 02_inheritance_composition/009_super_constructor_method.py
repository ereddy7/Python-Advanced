class Person:
    def __init__(self,name,age): self.name,self.age=name,age
    def display(self): print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,roll,marks): super().__init__(name,age); self.roll,self.marks=roll,marks
    def display(self): super().display(); print(self.roll,self.marks)
Student("Durga",22,101,90).display()
