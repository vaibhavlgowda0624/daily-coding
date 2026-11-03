import os

folders = ["src", "tests", "docs", "data"]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print("Created:", folder)
