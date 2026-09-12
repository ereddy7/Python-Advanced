class Test:
    def __init__(self): print("Constructor")
    def __del__(self): print("Destructor")
items=[Test(),Test(),Test()]; del items; print("End")
