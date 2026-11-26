import pandas as pd

data = {
    "Department": ["IT", "CSE", "IT", "CSE"],
    "Marks": [80, 90, 85, 95]
}

df = pd.DataFrame(data)

result = df.groupby("Department")["Marks"].mean()

print(result)
