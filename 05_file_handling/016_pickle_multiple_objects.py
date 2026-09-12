import pickle
records=[{"eno":100,"name":"Durga"},{"eno":200,"name":"Ravi"}]
with open("employees.dat","wb") as f:
    for obj in records: pickle.dump(obj,f)
with open("employees.dat","rb") as f:
    while True:
        try: print(pickle.load(f))
        except EOFError: break
