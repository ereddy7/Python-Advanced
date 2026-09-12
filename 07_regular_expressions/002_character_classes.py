import re
for pattern in (r"[abc]",r"[^abc]",r"[a-z]",r"[0-9]",r"[^a-zA-Z0-9]"):
    print(pattern,[(m.start(),m.group()) for m in re.finditer(pattern,"a7b@k9z")])
