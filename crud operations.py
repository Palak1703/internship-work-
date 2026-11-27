
students = {}

# CREATE
def create_student():
    student_id = int(input("Enter Student ID: "))

    if student_id in students:
        print("Student already exists!")

    else:
        name = input("Enter Student Name: ").strip()
        age = int(input("Enter Student Age: "))
        course = input("Enter Course: ").strip()

        students[student_id] = {
            "name": name,
            "age": age,
            "course": course
        }

        print("Student created successfully!")


# READ
def read_student():
    student_id = int(input("Enter Student ID: "))

    if student_id in students:
        print("\nStudent Details:")
        print("ID:", student_id)
        print("Name:", students[student_id]["name"])
        print("Age:", students[student_id]["age"])
        print("Course:", students[student_id]["course"])

    else:
        print("Student not found!")


# UPDATE
def update_student():
    student_id = int(input("Enter Student ID: "))

    if student_id in students:
        name = input("Enter New Name: ").strip()
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ").strip()

        students[student_id]["name"] = name
        students[student_id]["age"] = age
        students[student_id]["course"] = course

        print("Student updated successfully!")

    else:
        print("Student not found!")


# DELETE
def delete_student():
    student_id = int(input("Enter Student ID: "))

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")

    else:
        print("Student not found!")


# MAIN MENU
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Create Student")
    print("2. Read Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_student()

    elif choice == "2":
        read_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
