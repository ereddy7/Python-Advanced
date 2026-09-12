with open("abc.txt","w+",encoding="utf-8") as f:
    f.write("All Students are STUPIDS"); print(f.tell()); f.seek(17); f.write("GEMS!!!"); f.seek(0); print(f.read())
