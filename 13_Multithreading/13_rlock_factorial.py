from threading import RLock
l=RLock()
def fact(n):
    with l: return 1 if n==0 else n*fact(n-1)
print(fact(5))
