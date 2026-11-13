from datetime import date

dob = date(2004, 5, 15)
today = date.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Age:", age)
