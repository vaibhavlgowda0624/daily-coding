from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def stock_value(self):
        return self.price * self.quantity


product = Product("Keyboard", 1200, 5)

print(product)
print("Stock value:", product.stock_value())
