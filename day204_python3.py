import json

profile = {
    "username": "developer01",
    "skills": ["Python", "HTML", "SQL"],
    "active": True
}

json_text = json.dumps(profile, indent=4)

print(json_text)

restored_profile = json.loads(json_text)
print("Username:", restored_profile["username"])
