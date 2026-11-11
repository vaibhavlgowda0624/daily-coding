import string

def check_password(password):
    checks = {
        "Length": len(password) >= 12,
        "Uppercase": any(c.isupper() for c in password),
        "Lowercase": any(c.islower() for c in password),
        "Digit": any(c.isdigit() for c in password),
        "Special": any(c in string.punctuation for c in password)
    }

    for name, passed in checks.items():
        print(name, ":", "Passed" if passed else "Failed")


check_password("MySecure@12345")
