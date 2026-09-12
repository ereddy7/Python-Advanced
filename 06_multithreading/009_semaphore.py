from threading import Thread,Semaphore
import time
s=Semaphore(2)
def job(n):
    with s: print("start",n); time.sleep(.3); print("end",n)
ts=[Thread(target=job,args=(i,)) for i in range(5)]
for t in ts:t.start()
for t in ts:t.join()
