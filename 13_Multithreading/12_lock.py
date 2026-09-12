from threading import Thread,Lock
lock=Lock()
def wish(n):
    with lock:
        for _ in range(2): print("Good Evening",n)
ts=[Thread(target=wish,args=(n,)) for n in ("Dhoni","Yuvraj","Kohli")]
for t in ts:t.start()
for t in ts:t.join()
