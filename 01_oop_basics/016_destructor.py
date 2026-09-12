class Test:
    def __init__(self): print("Object initialized")
    def __del__(self): print("Cleanup before destruction")
t=Test(); del t; print("End")
