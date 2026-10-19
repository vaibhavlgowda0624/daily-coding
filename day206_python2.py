from datetime import datetime

date_text = input("Enter date (DD-MM-YYYY): ")

try:
    date = datetime.strptime(date_text, "%d-%m-%Y")

    if date.strftime("%d-%m-%Y") == date_text:
        print("Valid date:", date.date())
    else:
        print("Use DD-MM-YYYY format.")

except ValueError:
    print("Invalid date.")
