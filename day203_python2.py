import re

number = input("Enter mobile number: ").strip()

pattern = r'^[6-9]\d{9}$'

if re.fullmatch(pattern, number):
    print("Valid 10-digit mobile number")
else:
    print("Invalid mobile number")
