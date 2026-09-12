class Duck:
    def talk(self): print("Quack")
class Dog:
    def bark(self): print("Bow")
def speak(obj):
    if hasattr(obj,"talk"): obj.talk()
    elif hasattr(obj,"bark"): obj.bark()
for obj in (Duck(),Dog()): speak(obj)
