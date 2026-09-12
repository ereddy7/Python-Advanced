class Test:
    def __del__(self): print("Destructor")
t1=Test(); t2=t1; t3=t1; del t1; print("one deleted"); del t2; print("two deleted"); del t3
