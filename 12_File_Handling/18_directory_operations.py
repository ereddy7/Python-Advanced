import os,tempfile
with tempfile.TemporaryDirectory() as d:
    p=os.path.join(d,"sub"); os.mkdir(p); print(os.listdir(d)); os.rename(p,os.path.join(d,"new")); print(os.listdir(d))
