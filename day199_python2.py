inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

item = input("Enter item: ")
quantity = int(input("Enter quantity to add: "))

inventory[item] = inventory.get(item, 0) + quantity

print("Updated Inventory:")
print(inventory)
