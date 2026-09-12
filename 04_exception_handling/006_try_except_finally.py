try: print(10/0)
except ZeroDivisionError: print("Handled")
finally: print("Cleanup always runs")
