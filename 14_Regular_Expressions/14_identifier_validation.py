import re
s=input("Identifier:"); print("Valid" if re.fullmatch(r"[a-k][0369][a-zA-Z0-9#]*",s) else "Invalid")
