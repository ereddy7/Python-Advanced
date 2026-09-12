def decor(f):
    def inner(n): return "Special" if n=="Sunny" else f(n)
    return inner
def wish(n): return "Hello "+n
d=decor(wish); print(wish("Sunny")); print(d("Sunny"))
