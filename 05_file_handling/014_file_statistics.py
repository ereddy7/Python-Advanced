from pathlib import Path
from datetime import datetime
p=Path("abc.txt"); s=p.stat(); print(s.st_size,datetime.fromtimestamp(s.st_atime),datetime.fromtimestamp(s.st_mtime))
