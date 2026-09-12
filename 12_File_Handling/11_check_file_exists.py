import os
f="abc.txt"; print(open(f).read() if os.path.isfile(f) else "Not found")
