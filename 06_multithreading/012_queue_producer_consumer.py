from threading import Thread
from queue import Queue
q=Queue()
def producer():
    for x in range(5): q.put(x)
    q.put(None)
def consumer():
    while (x:=q.get()) is not None: print("Consumed",x)
    q.task_done()
Thread(target=consumer).start(); Thread(target=producer).start()
