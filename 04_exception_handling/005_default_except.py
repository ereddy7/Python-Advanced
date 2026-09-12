try:
    x=int(input("First:")); y=int(input("Second:")); print(x/y)
except ZeroDivisionError: print("Cannot divide by zero")
except Exception as error: print("Error:",error)
