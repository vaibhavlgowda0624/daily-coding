from datetime import datetime

date_input = input("Enter date (DD-MM-YYYY): ")

try:
    date = datetime.strptime(date_input, "%d-%m-%Y")
    print("Valid date:", date.strftime("%Y-%m-%d"))
except ValueError:
    print("Invalid date")
