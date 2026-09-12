class Student:
    def __init__(self,n,m): self.name,self.marks=n,m
    def __gt__(self,o): return self.marks>o.marks
    def __le__(self,o): return self.marks<=o.marks
s1=Student("Durga",100); s2=Student("Ravi",200); print(s1>s2,s1<=s2)
