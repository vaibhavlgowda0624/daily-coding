import json

products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Keyboard", "price": 1500},
    {"name": "Mouse", "price": 700}
]

with open("products.json", "w") as file:
    json.dump(products, file, indent=4)

print("Product data exported")
