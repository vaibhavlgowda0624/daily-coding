import csv

expenses = [
    {"category": "Food", "amount": 2500},
    {"category": "Travel", "amount": 1200},
    {"category": "Shopping", "amount": 1800}
]

with open("expense_report.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["category", "amount"]
    )

    writer.writeheader()
    writer.writerows(expenses)

print("Expense report created successfully.")
