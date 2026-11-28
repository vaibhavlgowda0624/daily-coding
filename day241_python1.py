from pathlib import Path

file = Path("sample.txt")

if file.exists():
    print("Name:", file.name)
    print("Extension:", file.suffix)
    print("Size:", file.stat().st_size, "bytes")
else:
    print("File not found")
