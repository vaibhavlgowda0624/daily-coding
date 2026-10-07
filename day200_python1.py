students = []

while True:
    print("\n--- Student Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))

        student = {
            "name": name,
            "course": course,
            "marks": marks
        }

        students.append(student)
        print("Student added.")

    elif choice == "2":
        for student in students:
            print(student)

    elif choice == "3":
        name = input("Enter student name: ")

        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                print(student)
                found = True

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
