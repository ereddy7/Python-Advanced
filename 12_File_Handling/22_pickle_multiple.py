import pickle
with open("emp.dat","wb") as f:
    for x in [{"id":1},{"id":2}]: pickle.dump(x,f)
with open("emp.dat","rb") as f:
    while True:
        try: print(pickle.load(f))
        except EOFError: break
