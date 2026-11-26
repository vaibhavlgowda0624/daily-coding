import pandas as pd

data = {
    "Name": ["Ravi", "Priya", "Aman"],
    "Marks": [80, 95, 75]
}

df = pd.DataFrame(data)

print(df)
print("Average:", df["Marks"].mean())
