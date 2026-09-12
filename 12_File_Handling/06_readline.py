open("abc.txt","w").write("sunny\nbunny\nchinny\n")
with open("abc.txt") as f:
    print(f.readline(),end=""); print(f.readline(),end="")
