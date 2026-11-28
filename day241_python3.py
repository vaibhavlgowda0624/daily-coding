from pathlib import Path

folder = Path(".")

files = [f for f in folder.iterdir() if f.is_file()]

if files:
    largest = max(files, key=lambda f: f.stat().st_size)
    print("Largest file:", largest.name)
    print("Size:", largest.stat().st_size, "bytes")
else:
    print("No files found")
