expenses = [
    {"category": "Food", "amount": 2500},
    {"category": "Travel", "amount": 1200},
    {"category": "Shopping", "amount": 1800},
    {"category": "Food", "amount": 1500}
]

monthly_total = sum(item["amount"] for item in expenses)

print("Monthly expenses:", monthly_total)
