class Engine:
    a=10
    def __init__(self): self.b=20
    def start(self): print("Engine started")
class Car:
    def __init__(self): self.engine=Engine()
    def use(self): print(self.engine.a,self.engine.b); self.engine.start()
Car().use()
