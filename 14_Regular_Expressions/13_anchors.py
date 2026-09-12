import re
s="Learning Python is Very Easy"; print(bool(re.search(r"^Learn",s))); print(bool(re.search(r"easy$",s,re.I)))
