class Duck:
    def talk(self): print("Quack")
class Dog:
    def bark(self): print("Bow")
def f(obj):
    if hasattr(obj,"talk"): obj.talk()
    elif hasattr(obj,"bark"): obj.bark()
for x in (Duck(),Dog()): f(x)
