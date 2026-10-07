expenses = {
    "Food": [250, 180, 320],
    "Travel": [100, 250],
    "Shopping": [800, 450],
    "Bills": [1200]
}

grand_total = 0

for category, values in expenses.items():
    total = sum(values)

    print(category, ":", total)

    grand_total += total

print("----------------")
print("Total Expenses:", grand_total)
