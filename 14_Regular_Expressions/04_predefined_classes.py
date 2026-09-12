import re
for p in (r"\s",r"\S",r"\d",r"\D",r"\w",r"\W",r"."): print(p,re.findall(p,"a7b k@9z"))
