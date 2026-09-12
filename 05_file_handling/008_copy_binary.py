from pathlib import Path
Path("newpic.jpg").write_bytes(Path("rossum.jpg").read_bytes())
print("Copied")
