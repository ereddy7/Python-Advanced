import re
for p in (r"a",r"a+",r"a*",r"a?",r"a{3}",r"a{2,4}"): print(p,re.findall(p,"abaabaaab"))
