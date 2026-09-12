from threading import Thread,Event
import time
event=Event()
def producer(): time.sleep(.5); print("Produced"); event.set()
def consumer(): print("Waiting"); event.wait(); print("Consumed")
Thread(target=consumer).start(); Thread(target=producer).start()
