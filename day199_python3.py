cart = {
    "Keyboard": 1200,
    "Mouse": 700,
    "Headphones": 1800
}

total = sum(cart.values())

if total >= 3000:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("Cart Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)
