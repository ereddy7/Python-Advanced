try: result=10/int(input("Divisor:"))
except (ValueError,ZeroDivisionError) as e: print(e)
else: print("Result:",result)
finally: print("Completed")
