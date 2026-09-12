def square(f):
    def inner(): return f()**2
    return inner
def double(f):
    def inner(): return 2*f()
    return inner
@square
@double
def num(): return 10
print(num())
