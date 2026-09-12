from zipfile import ZipFile
with ZipFile("files.zip") as z: print(z.namelist())
