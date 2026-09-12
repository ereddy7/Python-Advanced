import os
from datetime import datetime
open("abc.txt","a").close(); s=os.stat("abc.txt"); print(s.st_size,datetime.fromtimestamp(s.st_mtime))
