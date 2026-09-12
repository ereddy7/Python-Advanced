class InvalidAgeError(Exception): pass
age=int(input("Age:"))
if not 18<=age<=60: raise InvalidAgeError("Age must be between 18 and 60")
print("Valid age")
