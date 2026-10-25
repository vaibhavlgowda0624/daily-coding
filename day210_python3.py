import csv

expenses = [
    {"category": "Food", "amount": 250},
    {"category": "Travel", "amount": 120},
    {"category": "Books", "amount": 450},
    {"category": "Food", "amount": 180}
]

totals = {}

for expense in expenses:
    category = expense["category"]
    totals[category] = (
        totals.get(category, 0) + expense["amount"]
    )

with open("expense_report.csv", "w", newline="",
          encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Total Amount"])

    for category, amount in totals.items():
        writer.writerow([category, amount])

    writer.writerow(["Grand Total", sum(totals.values())])

print("Report exported to expense_report.csv")
