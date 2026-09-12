open("abc.txt","w").write("sunny\nbunny")
with open("abc.txt") as f: print(f.read(10))
