import os
for path,dirs,files in os.walk("."):
    print(path,dirs,files)
