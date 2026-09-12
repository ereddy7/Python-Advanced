def smart(func):
    def inner(a,b):
        if b==0: print("Cannot divide"); return None
        return func(a,b)
    return inner
@smart
def divide(a,b): return a/b
print(divide(20,2)); print(divide(20,0))
