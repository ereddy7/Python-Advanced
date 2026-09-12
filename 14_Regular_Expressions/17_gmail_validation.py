import re
s=input("Gmail:"); print("Valid" if re.fullmatch(r"[A-Za-z0-9_.]+@gmail\.com",s) else "Invalid")
