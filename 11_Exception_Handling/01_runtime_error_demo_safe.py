try: print(10/0)
except ZeroDivisionError as e: print(type(e).__name__,e)
