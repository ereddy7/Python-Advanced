from threading import Thread
class MyThread(Thread):
    def run(self): print("Child")
t=MyThread(); t.start(); t.join()
