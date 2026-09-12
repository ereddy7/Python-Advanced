open("abc.txt","w").write("sunny")
with open("abc.txt") as f: print(f.tell()); print(f.read(2)); print(f.tell())
