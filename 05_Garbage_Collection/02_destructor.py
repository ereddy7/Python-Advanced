class Test:
    def __init__(self): print("Object initialization")
    def __del__(self): print("Cleanup")
t=Test(); t=None; print("End")
