import re
s="ababab"
print(re.match(r"ab",s)); print(re.fullmatch(r"(?:ab){3}",s)); print(re.search(r"ba",s))
