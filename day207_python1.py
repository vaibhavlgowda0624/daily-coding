from pathlib import Path
import shutil

folder = Path("test_files")

for file in list(folder.iterdir()):
    if file.is_file():
        extension = file.suffix.lower().lstrip(".") or "no_extension"
        destination_folder = folder / extension
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / file.name

        if not destination.exists():
            shutil.move(str(file), str(destination))
            print("Moved:", file.name)
