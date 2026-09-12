from threading import Thread,current_thread
def job(): print(current_thread().name,current_thread().ident)
t=Thread(target=job,name="Worker"); t.start(); t.join()
