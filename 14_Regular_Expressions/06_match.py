import re
m=re.match(input("Pattern:"),"abcabdefg"); print(m.span() if m else "No match")
