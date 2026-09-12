import re
for pattern in (r"a",r"a+",r"a*",r"a?",r"a{3}",r"a{2,4}"):
    print(pattern,[m.group() for m in re.finditer(pattern,"abaabaaab")])
