def square(func):
    def inner(): return func()**2
    return inner
def double(func):
    def inner(): return 2*func()
    return inner
@square
@double
def num(): return 10
print(num())
