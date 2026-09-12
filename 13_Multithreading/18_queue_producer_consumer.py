from queue import Queue
from threading import Thread
q=Queue()
def p():
    for i in range(3): q.put(i)
    q.put(None)
def c():
    while (x:=q.get()) is not None: print(x)
t1=Thread(target=c); t2=Thread(target=p); t1.start(); t2.start(); t1.join(); t2.join()
