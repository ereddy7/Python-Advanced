import re
for m in re.compile("ab").finditer("abaababa"): print(m.start(),m.end(),m.group())
