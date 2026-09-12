open("abc.txt","w").write("sunny\nbunny\nchinny\nvinny\n")
with open("abc.txt") as f: print(f.read())
