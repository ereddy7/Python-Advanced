def smart(f):
    def inner(a,b): return "Cannot divide" if b==0 else f(a,b)
    return inner
@smart
def div(a,b): return a/b
print(div(20,2)); print(div(20,0))
