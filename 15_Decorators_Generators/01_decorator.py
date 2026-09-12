def decor(f):
    def inner(name): print("Special" if name=="Sunny" else f(name))
    return inner
@decor
def wish(name): return "Hello "+name
wish("Durga"); wish("Sunny")
