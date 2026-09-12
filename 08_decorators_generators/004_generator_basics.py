def mygen():
    yield "A"; yield "B"; yield "C"
for x in mygen(): print(x)
