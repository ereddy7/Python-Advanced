text="one two\nthree four\n"; open("abc.txt","w").write(text)
with open("abc.txt") as f: lines=f.readlines()
print(len(lines),sum(len(x.split()) for x in lines),sum(len(x) for x in lines))
