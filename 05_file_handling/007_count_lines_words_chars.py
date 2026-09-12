from pathlib import Path
text=Path(input("File name:")).read_text(encoding="utf-8")
print("Lines:",len(text.splitlines()),"Words:",len(text.split()),"Characters:",len(text))
