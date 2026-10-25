from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Processing card payment of ₹{amount}")


payments = [UpiPayment(), CardPayment()]

for payment in payments:
    payment.pay(500)
