import re
s=input("Registration:"); print("Valid" if re.fullmatch(r"TS[0-2][0-9][A-Z]{2}\d{4}",s) else "Invalid")
