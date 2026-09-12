import re
m=re.search(input("Pattern:"),"abaaaba"); print(m.span() if m else "No match")
