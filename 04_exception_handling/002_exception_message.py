try: print(10/0)
except ZeroDivisionError as error: print(type(error).__name__,error)
