open("abc.txt","w").write("sunny\nbunny\nchinny\n")
with open("abc.txt") as f:
    for line in f.readlines(): print(line,end="")
