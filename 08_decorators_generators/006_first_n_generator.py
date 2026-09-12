def first_n(n):
    yield from range(1,n+1)
print(list(first_n(10)))
