import json
from pathlib import Path

file_path = Path("contacts.json")

if file_path.exists():
    contacts = json.loads(file_path.read_text(encoding="utf-8"))
else:
    contacts = {}

name = input("Contact name: ").strip()
phone = input("Phone number: ").strip()

if name and phone:
    contacts[name] = phone

    file_path.write_text(
        json.dumps(contacts, indent=4),
        encoding="utf-8"
    )

    print("Contact saved.")
else:
    print("Name and phone are required.")
