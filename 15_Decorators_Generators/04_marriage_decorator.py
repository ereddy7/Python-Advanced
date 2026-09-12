def decor(f):
    def inner(): print("Decoration"); f()
    return inner
def ready(): print("Ready")
decor(ready)()
