import hashlib

def file_hash(path):
    sha = hashlib.sha256()

    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha.update(chunk)

    return sha.hexdigest()

print(file_hash("report.pdf"))
