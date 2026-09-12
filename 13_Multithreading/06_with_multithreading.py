from threading import Thread
def doubles(a):
    for n in a: print(2*n)
def squares(a):
    for n in a: print(n*n)
a=[1,2,3]; t1=Thread(target=doubles,args=(a,)); t2=Thread(target=squares,args=(a,)); t1.start(); t2.start(); t1.join(); t2.join()
