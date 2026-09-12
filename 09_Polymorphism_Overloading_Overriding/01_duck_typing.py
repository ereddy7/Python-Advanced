class Duck:
    def talk(self): print("Quack")
class Dog:
    def talk(self): print("Bow")
def f(obj): obj.talk()
for x in (Duck(),Dog()): f(x)
