from threading import Thread
class MyThread(Thread):
    def run(self):
        for _ in range(5): print("Child")
t=MyThread(); t.start(); t.join()
