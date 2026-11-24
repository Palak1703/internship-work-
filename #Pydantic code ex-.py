#Pydantic code ex- 
from pydantic import BaseModel

class User(BaseModel):# creates model
    name: str
    age: int
    email: str

user1 = User(. # creates obj of model
    name="Palak",
    age=21,
    email="palak@gmail.com"
)

print(user1.name). # to access obj of data 


 # field()
from pydantic import BaseModel, Field

class Employee(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt=18, lt=60)


# Field Validator

from pydantic import BaseModel, field_validator

class Student(BaseModel):

    name: str

    @field_validator("name")  #Name field ko validate karo
    @classmethod. # "@" - It tells Pydantic that this method is a validator. (decorator)
    def check_name(cls, value):
        if not value.isalpha():  # .isalpha - Check karta hai ki all characters letters hain
            raise ValueError("Name must contain only letters")

        return value



# model_validator

from pydantic import BaseModel, model_validator

class User(BaseModel):

    password: str
    confirm_password: str

    @model_validator(mode="after")
    def check_password(self):

        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")

        return self

#crud learning!
student = {}

# CREATE FUNCTION
def create_student():
    student_id = int(input("Enter student_id: "))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")
    
    if student_id in student:
        print(" ID already EXISTS ")
    else:
        student[student_id] = {
        "name": name,
        "age": age,
        "course": course
        }
        print("Student created successfully")

# READ fucntion
def read_student():
    student_id = int(input("Enter student_id: "))

    if student_id in student:
        print(student[student_id])
    else:
        print("Student not found")

def update_student():
    student_id = int(input("Enter student_id: "))

    if student_id in student:

        new_age = int(input("Enter updated age: "))
        student[student_id]["age"] = new_age
        print("student age updated successfully!!")
    else:
        print("Student not found")


# FUNCTION CALL
create_student()
read_student()
update_student()
