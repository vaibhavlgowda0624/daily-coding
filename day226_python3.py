from collections import Counter

login_attempts = [
    "192.168.1.10",
    "192.168.1.12",
    "192.168.1.10",
    "192.168.1.10",
    "192.168.1.15",
    "192.168.1.12"
]

counts = Counter(login_attempts)

for ip, attempts in counts.items():
    if attempts >= 3:
        print("Repeated attempts:", ip, attempts)
