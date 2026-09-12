import re
s="a7b9c5k8z"
print(re.findall(r"[0-9]",s)); print(re.sub(r"[a-z]","#",s)); print(re.subn(r"[a-z]","#",s)); print(re.split(r"[0-9]",s))
