import re
for pattern in (r"\s",r"\S",r"\d",r"\D",r"\w",r"\W",r"."):
    print(pattern,re.findall(pattern,"a7b k@9z"))
