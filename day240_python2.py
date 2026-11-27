keywords = [
    "failed login",
    "unauthorized",
    "suspicious",
    "access denied"
]

with open("security.log", "r") as file:
    logs = file.readlines()

for line_number, line in enumerate(logs, start=1):
    if any(word in line.lower() for word in keywords):
        print(f"Alert at line {line_number}: {line.strip()}")
