class Book:
    def __init__(self,pages): self.pages=pages
    def __add__(self,other): return self.pages+other.pages
print(Book(100)+Book(200))
