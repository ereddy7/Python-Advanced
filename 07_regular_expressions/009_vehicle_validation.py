import re
number=input("Registration:")
print("Valid" if re.fullmatch(r"TS[0-2][0-9][A-Z]{2}\d{4}",number) else "Invalid")
