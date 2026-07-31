def withdraw(balance, amount):

    if amount <= 0:
        raise ValueError("Amount must be positive.")

    if amount > balance:
        raise ValueError("Insufficient funds.")

    return balance - amount


print(withdraw(500, 200))

print(withdraw(500, 900))  # This will raise a ValueError: Insufficient funds.

print(withdraw(500, -10))  # This will raise a ValueError: Amount must be positive. 

