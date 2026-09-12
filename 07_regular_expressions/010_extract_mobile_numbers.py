import re
from pathlib import Path
text=Path("input.txt").read_text(encoding="utf-8")
Path("output.txt").write_text("\n".join(re.findall(r"(?<!\d)[7-9]\d{9}(?!\d)",text)),encoding="utf-8")
