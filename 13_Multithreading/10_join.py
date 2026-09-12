from threading import Thread
def job(): print("Seetha")
t=Thread(target=job); t.start(); t.join(); print("Rama")
