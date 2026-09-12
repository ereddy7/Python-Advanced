class Duck:
    def talk(self): print("Quack")
class Dog:
    def talk(self): print("Bow")
def speak(obj): obj.talk()
for obj in (Duck(),Dog()): speak(obj)
