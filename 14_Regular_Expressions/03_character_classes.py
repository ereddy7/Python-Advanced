import re
for p in (r"[abc]",r"[^abc]",r"[a-z]",r"[0-9]",r"[^a-zA-Z0-9]"): print(p,re.findall(p,"a7b@k9z"))
