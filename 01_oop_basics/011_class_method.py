class Animal:
    legs=4
    @classmethod
    def walk(cls,name): print(name,"walks with",cls.legs,"legs")
Animal.walk("Dog"); Animal.walk("Cat")
