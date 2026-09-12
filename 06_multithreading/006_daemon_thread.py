import threading,time
def job():
    while True: print("daemon working"); time.sleep(.2)
t=threading.Thread(target=job,daemon=True); t.start(); time.sleep(.7); print("Main ends")
