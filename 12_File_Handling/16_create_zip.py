from zipfile import ZipFile,ZIP_DEFLATED
for n in ("file1.txt","file2.txt","file3.txt"): open(n,"w").write(n)
with ZipFile("files.zip","w",ZIP_DEFLATED) as z:
    for n in ("file1.txt","file2.txt","file3.txt"): z.write(n)
