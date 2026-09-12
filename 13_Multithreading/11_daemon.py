from threading import Thread
t=Thread(target=lambda:print("daemon"),daemon=True); print(t.daemon); t.start(); t.join()
