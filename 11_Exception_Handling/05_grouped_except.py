try:
    x=int(input("First:")); y=int(input("Second:")); print(x/y)
except (ZeroDivisionError,ValueError) as e: print("Invalid:",e)
