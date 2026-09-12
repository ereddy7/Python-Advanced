from zipfile import ZipFile,ZIP_DEFLATED
with ZipFile("files.zip","w",ZIP_DEFLATED) as z:
    for name in ("file1.txt","file2.txt","file3.txt"): z.write(name)
