import hashlib

def calculate_hash(path):
    with open(path, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()


file1 = calculate_hash("original.txt")
file2 = calculate_hash("copy.txt")

if file1 == file2:
    print("Files have identical content")
else:
    print("Files differ")
