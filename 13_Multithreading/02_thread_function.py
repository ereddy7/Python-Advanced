from threading import Thread
def display():
    for _ in range(3): print("Child")
t=Thread(target=display); t.start(); t.join(); print("Main")
