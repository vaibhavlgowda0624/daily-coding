from collections import defaultdict

expenses = [
    ("Food", 2500),
    ("Travel", 1200),
    ("Shopping", 1800),
    ("Food", 1500)
]

category_total = defaultdict(int)

for category, amount in expenses:
    category_total[category] += amount

for category, total in category_total.items():
    print(category, ":", total)
