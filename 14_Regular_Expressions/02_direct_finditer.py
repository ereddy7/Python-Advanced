import re
for m in re.finditer("ab","abaababa"): print(m.start(),m.end(),m.group())
