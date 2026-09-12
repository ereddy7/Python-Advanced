try:
    print("outer")
    try: print(10/0)
    except ZeroDivisionError: print("inner handled")
    finally: print("inner finally")
finally: print("outer finally")
