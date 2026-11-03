import hashlib
from pathlib import Path

folder = Path("test_files")
seen = {}

for file in folder.iterdir():
    if file.is_file():
        digest = hashlib.sha256(file.read_bytes()).hexdigest()

        if digest in seen:
            print("Duplicate:", file.name, "matches", seen[digest])
        else:
            seen[digest] = file.name
