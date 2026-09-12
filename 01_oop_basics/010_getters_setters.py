class Student:
    def set_name(self,name): self.name=name
    def get_name(self): return self.name
    def set_marks(self,marks): self.marks=marks
    def get_marks(self): return self.marks
s=Student(); s.set_name("Durga"); s.set_marks(100); print(s.get_name(),s.get_marks())
