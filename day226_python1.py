import hashlib

def calculate_hash(filename):
    digest = hashlib.sha256()

    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            digest.update(chunk)

    return digest.hexdigest()


print(calculate_hash("student.txt"))
