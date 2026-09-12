class Student:
    def setName(self,n): self.name=n
    def getName(self): return self.name
    def setMarks(self,m): self.marks=m
    def getMarks(self): return self.marks
s=Student(); s.setName("Durga"); s.setMarks(100); print(s.getName(),s.getMarks())
