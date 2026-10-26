def valid_password(password):
    return len(password) >= 8

assert valid_password("hello123") is True
assert valid_password("abc") is False
print("Password tests passed!")
