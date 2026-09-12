data="All Students are STUPIDS"
with open("abc.txt","w+") as f: f.write(data); f.seek(17); f.write("GEMS!!!"); f.seek(0); print(f.read())
