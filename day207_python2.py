from pathlib import Path

folder = Path("test_files")
limit_mb = 5
limit_bytes = limit_mb * 1024 * 1024

for file in folder.rglob("*"):
    if file.is_file() and file.stat().st_size > limit_bytes:
        size_mb = file.stat().st_size / (1024 * 1024)
        print(f"{file.name}: {size_mb:.2f} MB")
