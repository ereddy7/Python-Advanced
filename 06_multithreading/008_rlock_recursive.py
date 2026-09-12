from threading import RLock,Thread
lock=RLock()
def factorial(n):
    with lock: return 1 if n==0 else n*factorial(n-1)
def result(n): print(n,factorial(n))
for n in (5,9): Thread(target=result,args=(n,)).start()
