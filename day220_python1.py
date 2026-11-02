habits = {}

while True:
    print("\n1. Add habit")
    print("2. View habits")
    print("3. Mark complete")
    print("4. Exit")

    choice = input("Choose: ").strip()

    if choice == "1":
        habit = input("Habit name: ").strip()
        if habit:
            habits[habit] = False
            print("Habit added.")

    elif choice == "2":
        for name, completed in habits.items():
            status = "Done" if completed else "Pending"
            print(name, "-", status)

    elif choice == "3":
        habit = input("Habit to complete: ").strip()
        if habit in habits:
            habits[habit] = True
            print("Habit completed.")
        else:
            print("Habit not found.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
