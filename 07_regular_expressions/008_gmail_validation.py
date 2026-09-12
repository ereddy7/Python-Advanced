import re
email=input("Gmail:")
print("Valid" if re.fullmatch(r"[A-Za-z0-9_.]+@gmail\.com",email) else "Invalid")
