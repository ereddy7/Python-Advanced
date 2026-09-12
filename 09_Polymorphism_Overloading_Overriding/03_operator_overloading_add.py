class Book:
    def __init__(self,p): self.pages=p
    def __add__(self,o): return self.pages+o.pages
print(Book(100)+Book(200))
