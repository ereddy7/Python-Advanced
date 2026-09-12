from threading import Thread,Lock
lock=Lock()
def wish(name):
    with lock:
        for _ in range(3): print("Good Evening",name)
threads=[Thread(target=wish,args=(n,)) for n in ("Dhoni","Yuvraj","Kohli")]
for t in threads:t.start()
for t in threads:t.join()
