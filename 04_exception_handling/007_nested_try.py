try:
    print("Outer try")
    try: print(10/0)
    except ZeroDivisionError: print("Inner handled")
    finally: print("Inner finally")
except Exception: print("Outer handled")
finally: print("Outer finally")
