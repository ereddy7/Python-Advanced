import re
s=input("Mobile:"); print("Valid" if re.fullmatch(r"[7-9]\d{9}",s) else "Invalid")
