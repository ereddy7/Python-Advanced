from threading import Thread
def show(items):
    for x in items: print(x)
t=Thread(target=show,args=([1,2,3],),name="Worker"); t.start(); t.join(); print(t.name,t.ident,t.is_alive())
