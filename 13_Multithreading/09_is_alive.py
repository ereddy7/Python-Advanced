from threading import Thread
import time
t=Thread(target=lambda:time.sleep(.1)); t.start(); print(t.is_alive()); t.join(); print(t.is_alive())
