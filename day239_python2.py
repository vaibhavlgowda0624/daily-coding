import pandas as pd

data = {
    "Name": ["Ravi", "Priya", "Aman", "Neha"],
    "Marks": [65, 92, 78, 88]
}

df = pd.DataFrame(data)

top_students = df[df["Marks"] >= 80]

print(top_students)
