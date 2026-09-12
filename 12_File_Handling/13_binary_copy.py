from pathlib import Path
Path("source.bin").write_bytes(b"Python"); Path("copy.bin").write_bytes(Path("source.bin").read_bytes()); print(Path("copy.bin").read_bytes())
