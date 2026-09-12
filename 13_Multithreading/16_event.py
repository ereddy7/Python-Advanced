from threading import Thread,Event
e=Event()
def c(): print("waiting"); e.wait(); print("consumed")
def p(): print("produced"); e.set()
t1=Thread(target=c); t2=Thread(target=p); t1.start(); t2.start(); t1.join(); t2.join()
