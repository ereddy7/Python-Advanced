class Human:
    def __init__(self): self.head=self.Head(); self.brain=self.Brain()
    class Head:
        def talk(self): print("Talking")
    class Brain:
        def think(self): print("Thinking")
h=Human(); h.head.talk(); h.brain.think()
