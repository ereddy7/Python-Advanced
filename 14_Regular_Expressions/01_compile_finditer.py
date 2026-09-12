import re
p=re.compile("ab")
for m in p.finditer("abaababa"): print(m.start(),m.end(),m.group())
