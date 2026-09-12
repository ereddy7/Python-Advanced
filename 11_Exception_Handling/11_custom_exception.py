class InvalidAge(Exception): pass
age=int(input("Age:"))
if not 18<=age<=60: raise InvalidAge("Age must be 18 to 60")
print("Valid")
