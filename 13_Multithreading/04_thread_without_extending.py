from threading import Thread
class Test:
    def display(self): print("Child")
t=Thread(target=Test().display); t.start(); t.join()
