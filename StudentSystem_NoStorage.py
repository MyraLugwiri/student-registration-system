# --------------------- SCHOOL MANAGEMENT SYSTEM ---------------------------


class User:
    """This class gets the email, user_id, role and name of the user in the school"""

    def __init__(self, user_id, name, email, role):
        """Initializing the instance variables of the class"""

        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role

    def get_user_id(self):
        """returns the ID of the user in the school"""
        return f"{self.user_id}"

    def get_name(self):
        """returns the name of the user"""
        return f"{self.name}"

    def get_email(self):
        """returns the email address of the user"""
        # name_split = self.name.split()
        # valid_email = "{}.{}@agblschool.com".format(self.name[:1].lower(), name_split[1].lower())
        # if self.email != valid_email or self.email == "":
        #     print("Invalid email")
        return f"{self.email}"

    def get_role(self):
        """returns the role of the user in the school"""
        return f"{self.role}"

    def user_details(self):
        """displays information about the user"""
        name_split = self.name.split()
        valid_email = "{}.{}@agblschool.com".format(self.name[:1].lower(), name_split[1].lower())
        if self.email != valid_email or self.email == "":
            raise Exception("Invalid email")

        else:
            return "------------------------------ PERSONAL INFORMATION -----------------------" \
                   "\nUser ID: {}" \
                   "\nName: {}" \
                   "\nEmail: {}" \
                   "\nRole: {}".format(self.user_id, self.name, self.email, self.role)


class Student(User):
    """The class gets all information to register a particular student"""

    def __init__(self, user_id, name, email, role):
        super().__init__(user_id, name, email, role)
        self.dob = str
        self.age = str
        self.gender = str
        self.parent_name = str
        self.parent_contact = str
        self.address = str
        self.doA = str

    def get_dob(self):
        """returns the date of birth of the student"""
        print(f"{self.dob}")

    def get_age(self):
        """returns the age of the student"""
        print(f"{self.age}")

    def get_gender(self):
        """returns the gender of the student"""
        print(f"{self.gender}")

    def get_parent_name(self):
        """returns the students' parents' name"""
        print(f"{self.parent_name}")

    def get_parent_contact(self):
        """returns the students' parents' contact"""
        print(f"{self.parent_contact}")

    def set_parent_contact(self, phone_num):
        """returns the updated parent contact"""
        self.parent_contact = phone_num
        return f"{phone_num}"

    def get_address(self):
        """returns the address of the student"""
        print(f"{self.address}")

    def set_address(self, new_address):
        """returns the updated address"""
        self.address = new_address
        return f"{new_address}"

    def get_doA(self):
        """returns the date of admission of the student"""
        print(f"{self.doA}")

    def user_detail(self, dob, age, gender, parent_name, parent_contact, address, doA):
        """returns the information of the student"""
        name_split = self.name.split()
        valid_email = "{}.{}@agblschool.com".format(self.name[:1].lower(), name_split[1].lower())
        if self.email != valid_email or self.email == "":
            print("Invalid email")
        else:
            self.dob = dob
            self.age = age
            self.gender = gender
            self.parent_name = parent_name
            self.parent_contact = parent_contact
            self.address = address
            self.doA = doA
            return f"------------------------------ PERSONAL INFORMATION -----------------------"\
                  f"\nUser ID: {self.get_user_id()}"\
                  f"\nName: {self.get_name()}"\
                  f"\nEmail: {self.get_email()}"\
                  f"\nRole: {self.get_role()}"\
                  f"\nDate of Birth: {self.dob}"\
                  f"\nAge: {self.age}"\
                  f"\nGender: {self.gender}"\
                  f"\nParent name: {self.parent_name}"\
                  f"\nParent contact: {self.parent_contact}"\
                  f"\nAddress: {self.address}"\
                  f"\nDate of Admission: {self.doA}"


class Register(Student, User):
    """The student class the methods to register, search, delete, update or display students information in the
    registration system"""

    def __init__(self, user_id, name, email, role):
        super(Register, self).__init__(user_id, name, email, "student")
        self.student_list = []
        self.student_details = {"IB200": ["Irene Busah", "i.busah@agblschool.com", "student", "5th May, 2000", "21",
                                          "Female", "Joseph Busah", "+233549185709", "Takoradi", "30th December"],
                                "NN233": ["Nelson Nor", "n.nor@agblschool.com", "student", "10th May 2001", "20",
                                          "Male", "Constance Nor", "+233241918971", "Wa", "30th August 2020"]}
        self.num_of_students = 2

    def register(self, name, email, role, dob, age, gender, parent_name, parent_contact, address, doA):
        """Allows the user to register a new student"""
        self.student_list.append(name)
        self.student_list.append(email)
        self.student_list.append(role)
        self.student_list.append(dob)
        self.student_list.append(age)
        self.student_list.append(gender)
        self.student_list.append(parent_name)
        self.student_list.append(parent_contact)
        self.student_list.append(address)
        self.student_list.append(doA)
        self.student_details[self.get_user_id()] = list(self.student_list)
        self.num_of_students += 1
        # print(self.student_details)
        print(self.user_detail(dob, age, gender, parent_name, parent_contact, address, doA))

        print(f"---------------------SUCCESSFULLY REGISTERED {self.num_of_students}-----------------------")

    def delete_student(self, ID):
        """removes a student from the register"""
        if ID not in self.student_details.keys() or ID == "":
            raise Exception("ID not found")
        elif ID in self.student_details.keys():
            del self.student_details[ID]
            self.num_of_students -= 1
            return f"You have successfully deleted {ID} from the register system\n" \
                   f"Current Number of students: {self.num_of_students}\n" \
                   "----------------------- SUCCESSFULLY DELETED ----------------------"

    def search_student(self, ID):
        """returns the details of the student with the provided ID"""
        for student in list(self.student_details.keys()):
            if student == ID:
                print("Name: {}".format(self.student_details.get(ID)[0]))
                print("Email: {}".format(self.student_details.get(ID)[1]))
                print("Role: {}".format(self.student_details.get(ID)[2]))
                print("Date of birth: {}".format(self.student_details.get(ID)[3]))
                print("Age: {}".format(self.student_details.get(ID)[4]))
                print("Gender: {}".format(self.student_details.get(ID)[5]))
                print("Parent name: {}".format(self.student_details.get(ID)[6]))
                print("Parent contact: {}".format(self.student_details.get(ID)[7]))
                print("Address: {}".format(self.student_details.get(ID)[8]))
                print("Date of Admission: {}".format(self.student_details.get(ID)[8]))

    def update_student(self, user_id, new_address, new_parent_contact):
        """updates the address and parent_contact of the student in the register system
        using the set_parent_contact and set_address methods in the Student class
        """
        for key, value in self.student_details.items():
            if key in self.student_details.keys() and key == user_id:
                value[8] = self.set_address(new_address)
                value[7] = self.set_parent_contact(new_parent_contact)
                print(self.student_details.get(user_id))
                print("")
                print(f"-------------------- SUCCESSFULLY UPDATED --------------------")
            elif user_id not in self.student_details.keys():
                raise Exception("ID not found")

    def display_register(self):
        """returns the students in the register"""
        # for key, value in self.student_details.items():
        print(self.student_details)
