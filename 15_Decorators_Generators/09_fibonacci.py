def fib():
    a,b=0,1
    while True: yield a; a,b=b,a+b
for x in fib():
    if x>100: break
    print(x)
