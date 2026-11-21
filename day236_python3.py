from collections import defaultdict

logs = [
    ("vaibhav", "SUCCESS"),
    ("admin", "FAILED"),
    ("admin", "FAILED"),
    ("vaibhav", "SUCCESS"),
    ("admin", "FAILED")
]

failed = defaultdict(int)

for username, status in logs:
    if status == "FAILED":
        failed[username] += 1

for username, count in failed.items():
    if count >= 3:
        print("Alert:", username, "has", count, "failed logins")
