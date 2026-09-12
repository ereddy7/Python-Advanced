from pathlib import Path
p=Path(input("File name:"))
print(p.read_text(encoding="utf-8") if p.is_file() else "File does not exist")
