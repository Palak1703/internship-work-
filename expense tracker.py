
expenses = {}

# POST - CREATE
def add_expense():
    expense_id = int(input("Enter Expense ID: "))
    amount = int(input("Enter Amount: "))
    category = input("Enter Category: ")

    if expense_id in expenses:
        print("400 - Expense already exists")
    else:
        expenses[expense_id] = {
            "amount": amount,
            "category": category
        }
        print("201 - Expense Created")


# GET - READ
def get_expenses():
    if not expenses:
        print("404 - No Expenses Found")
    else:
        for expense_id, details in expenses.items():
            print(expense_id, details)

        print("200 - Data Fetched")


# PUT - COMPLETE UPDATE
def update_expense():
    expense_id = int(input("Enter Expense ID: "))

    if expense_id in expenses:
        amount = int(input("Enter New Amount: "))
        category = input("Enter New Category: ")

        expenses[expense_id] = {
            "amount": amount,
            "category": category
        }

        print("200 - Expense Updated")
    else:
        print("404 - Expense Not Found")


# PATCH - PARTIAL UPDATE
def patch_expense():
    expense_id = int(input("Enter Expense ID: "))

    if expense_id in expenses:
        category = input("Enter New Category: ")

        expenses[expense_id]["category"] = category

        print("200 - Category Updated")
    else:
        print("404 - Expense Not Found")


# DELETE
def delete_expense():
    expense_id = int(input("Enter Expense ID: "))

    if expense_id in expenses:
        del expenses[expense_id]
        print("200 - Expense Deleted")
    else:
        print("404 - Expense Not Found")


# MAIN MENU
while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. POST - Add Expense")
    print("2. GET - View Expenses")
    print("3. PUT - Update Expense")
    print("4. PATCH - Update Category")
    print("5. DELETE - Delete Expense")
    print("6. EXIT")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        get_expenses()

    elif choice == "3":
        update_expense()

    elif choice == "4":
        patch_expense()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        break

    else:
        print("Invalid Choice")
