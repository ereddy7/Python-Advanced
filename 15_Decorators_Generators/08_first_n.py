def firstn(n):
    yield from range(1,n+1)
print(list(firstn(10)))
