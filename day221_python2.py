import os

folder = "test_files"

for index, filename in enumerate(os.listdir(folder), start=1):
    old_path = os.path.join(folder, filename)

    if os.path.isfile(old_path):
        extension = os.path.splitext(filename)[1]
        new_name = f"file_{index}{extension}"
        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)
        print("Renamed:", filename)
