from threading import Thread,Condition
c=Condition(); items=[]
def consume():
    with c: c.wait_for(lambda:items); print(items.pop())
def produce():
    with c: items.append(42); c.notify()
t1=Thread(target=consume); t2=Thread(target=produce); t1.start(); t2.start(); t1.join(); t2.join()
