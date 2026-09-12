with open("abc.txt","w",encoding="utf-8") as f:
    print(f.name,f.mode,f.readable(),f.writable(),f.closed)
print(f.closed)
