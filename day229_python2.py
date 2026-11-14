class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")

    return balance - amount


try:
    print(withdraw(1000, 1200))
except (ValueError, InsufficientBalanceError) as error:
    print("Error:", error)
