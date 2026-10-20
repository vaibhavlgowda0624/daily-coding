from pathlib import Path
from datetime import datetime
import shutil

source = Path("important.txt")

if source.exists():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = source.with_name(
        f"{source.stem}_{timestamp}{source.suffix}"
    )

    shutil.copy2(source, backup)
    print("Backup created:", backup)
else:
    print("Source file not found.")
