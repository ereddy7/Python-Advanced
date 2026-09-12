import re
s=input("Mobile:"); print("Valid" if re.fullmatch(r"(?:0|91)?[7-9]\d{9}",s) else "Invalid")
