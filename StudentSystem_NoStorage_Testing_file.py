# This file runs the methods in the W13_Summative_Q2_project_group_15

from StudentSystem_NoStorage import *


"""Welcome the user to the register system"""

print("\nWelcome to the School Registration System")
print("")
print("------------------------- WELCOME ----------------------")
print("")
print("")
print("What would you like to do?\t"
      "\n1. Register a new student \n2. Update student details \n3. Search for a student \n4. Display "
      "students in "
      "the register \n5. Delete a student")
print("")
option = int(input("Choose your option: "))
print("")
try:
    user_id = input("Enter the student's ID(IB***): ")
    name = input("Enter the student's name(firstname & lastname): ")
    email = input("Enter the student's email (firstnameinitial.lastname@agblschool.com): ")
    role = "Student"
    if user_id == "" or name == "" or email == "" or role == "":
        print("Invalid ID or name or email or role")
        quit()

    else:
        user = User(user_id=user_id, name=name, email=email, role=role)
        print("")
        print(user.user_details())
        print("")
        print("You have successfully logged in")
        print("")

    students = Student(user_id, name, email, role)
    register = Register(user_id, name, email, role)
    if option == 1:
        """registers a new student"""
        ID = input("Enter the student's ID(IB***): ")
        std_name = input("Enter the student's name(firstname & lastname): ")
        std_email = input("Enter the student's email (firstnameinitial.lastname@agblschool.com): ")
        roles = "Student"
        dob = input("Enter the student's date of birth(dd/mm/yyyy): ")
        age = input("Enter the student's age: ")
        gender = input("Student gender (Male or Female): ")
        parent_name = input("Enter student's parent name(mother or father): ")
        parent_contact = input("Enter parent's contact: ")
        address = input("Enter student's address: ")
        doA = input("Enter date of admission: ")
        register = Register(ID, std_name, std_email, roles)
        register.register(std_name, std_email, roles, dob, age, gender, parent_name, parent_contact, address, doA)
    elif option == 2:
        """updates the details of the student"""
        print("")
        print("You have the chance to change your address or parent contact")
        print("")
        ID = input("Provide the ID of the student you want to update: ")
        new_contact = input("Provide the new contact number: ")
        new_address = input("Provide the new address: ")
        register.update_student(ID, new_address, new_contact)
    elif option == 3:
        """searches for a particular student"""
        ID = input("Enter the ID of the student: ")
        (register.search_student(ID))
    elif option == 4:
        """Display the students in the register system"""
        register.display_register()
    elif option == 5:
        """removes a student from the register system"""
        ID = input("Enter the ID of the student you want to delete: ")
        print("")
        print(register.delete_student(ID))


except Exception as ex:
    print(ex)

# user_id = input("Enter the student ID: ")
# name = input("Enter the student name: ")
# email = input("Enter the student email: ")
# role = input("Enter the role: ")


# def main():
#     while True:
#         greetings()
#         Registration()
#         restart = input("Would you like to do anything else? (Y/N) ")
#         if restart.upper() in ("NO", "N"):
#             print("")
#             print("************************** THANK YOU FOR USING OUR SERVICES ************************")
#             break
#
#
# main()
