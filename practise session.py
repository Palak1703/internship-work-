# GET - Read
def get_student():
    print("Student data fetched")

# POST - Create
def create_student():
    print("Student created")

# PUT - Complete update
def update_student():
    print("Student completely updated")

# PATCH - Partial update
def update_age():
    print("Student age updated")

# DELETE - Delete
def delete_student():
    print("Student deleted")


get_student()
create_student()
update_student()
update_age()
delete_student()

#HTTP Status Codes
status_codes = {
    200: "OK - Request successful",
    201: "Created - New data created",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error"
}

for code, message in status_codes.items():
    print(code, message)