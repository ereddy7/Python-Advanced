from zipfile import ZipFile
with ZipFile("files.zip") as z:
    print(z.namelist())
    for name in z.namelist(): print(name,z.read(name).decode())
