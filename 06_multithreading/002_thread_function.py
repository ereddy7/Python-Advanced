from threading import Thread
def display():
    for _ in range(5): print("Child Thread")
t=Thread(target=display); t.start()
for _ in range(5): print("Main Thread")
t.join()
