from collections import Counter

with open("security.log", "r") as file:
    logs = file.readlines()

levels = Counter()

for log in logs:
    for level in ("INFO", "WARNING", "ERROR"):
        if log.startswith(level):
            levels[level] += 1

print("Log Summary")

for level, count in levels.items():
    print(level, ":", count)
