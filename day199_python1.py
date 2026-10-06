inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

item = input("Enter item name: ")

if item in inventory:
    print("Available Quantity:", inventory[item])
else:
    print("Item not found.")
