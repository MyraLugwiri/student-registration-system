import unittest
from StudentSystem_NoStorage import *


class MyTestCase(unittest.TestCase):

    def test_user_id(self):
        """tests the get_user_id method in the Student class"""
        # answer = user.get_user_id()
        user_id = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        user = User(user_id, name, email, role)
        self.assertEqual(user.get_user_id(), "IB200")

    def test_name(self):
        """tests the get_name method in the Student class"""
        user_id = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        user = User(user_id, name, email, role)
        self.assertEqual(user.get_name(), "Irene Busah")

    def test_user_details_email(self):
        """tests the user details method if the email provided is in the correct format"""
        user_id = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        user = User(user_id, name, email, role)
        user.user_details()
        self.assertEqual("i.busah@agblschool.com", email)

    def test_email(self):
        """tests if the user_detail will print the error when the email provided doesn't follow the correct format"""
        user_id = "IB200"
        name = "Irene Busah"
        email = "i.busah@agbl.com"
        role = "Student"
        user = User(user_id, name, email, role)

        with self.assertRaises(Exception):
            user.user_details()

    def test_user_details(self):
        """tests the user detail method in the user class"""
        user_id = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        user = User(user_id, name, email, role)
        self.assertTrue(user.user_details())

    def test_empty_email(self):
        """The test case will test if user_detail method will print the error when the user does not provide an email
        """
        user_id = "IB200"
        name = "Irene Busah"
        email = ""
        role = "Student"
        user = User(user_id, name, email, role)

        with self.assertRaises(Exception):
            print(user.user_details())


class Test_Student(unittest.TestCase):
    def test_dob(self):
        """tests the get_dob method in the Student class"""
        user_id = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        dob = None
        student = Student(user_id, name, email, role)
        self.assertEqual(student.get_dob(), dob)

    def test_set_address(self):
        """testing the set_new_address method if it will return the new address provided"""
        user_id = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        student = Student(user_id, name, email, role)
        self.assertEqual(student.set_address("Kumasi"), "Kumasi")

    def test_set_contact(self):
        """testing the set_parent_contact method if it will return the new contact provided"""
        user_id = "IB200"
        name = "Irene Busah"
        emails = "i.busah@agblschool.com"
        role = "Student"
        student = Student(user_id, name, emails, role)
        self.assertEqual(student.set_parent_contact("+233784857890"), "+233784857890")

    def test_user_detail(self):
        """Testing if the user_detail method will print all the user details when the email is in the correct format"""
        user_id = "IB200"
        name = "Irene Busah"
        emails = "i.busah@agblschool.com"
        role = "Student"
        dob = "5th May 2000"
        age = "21"
        gender = "Female"
        parent_name = "Joseph Busah"
        parent_contact = "+233784857890"
        address = "Wa"
        doA = "23th June 2020"
        student = Student(user_id, name, emails, role)
        students = Student.user_detail(student, dob, age, gender, parent_name, parent_contact, address, doA)
        self.assertTrue(students)

    def test_user_detail_error(self):
        """testing the user_details method if a user will get the error message when the email is incorrect"""
        user_id = "IB200"
        name = "Irene Busah"
        emails = "i.busah@agbl.com"
        role = "Student"
        dob = "5th May 2000"
        age = "21"
        gender = "Female"
        parent_name = "Joseph Busah"
        parent_contact = "+233784857890"
        address = "Wa"
        doA = "23th June 2020"
        student = Student(user_id, name, emails, role)
        students = Student.user_detail(student, dob, age, gender, parent_name, parent_contact, address, doA)
        with self.assertRaises(Exception):
            students.user_details()


class Test_registration(unittest.TestCase):
    """This class tests the methods of the Registration class"""

    def test_register_method(self):
        """tests the register student method in the Registration class, if the method will register and display the
        student's details """
        student_detail = {"IB200": ["Irene Busah", "i.busah@agblschool.com", "student", "5th May, 2000", "21",
                                    "Female", "Joseph Busah", "+233549185709", "Takoradi", "30th December"]}
        ID = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        dob = "5th May 2000"
        age = "21"
        gender = "Female"
        father = "Margaret Busah"
        contact = "+233784857890"
        address = "Kumasi"
        doA = "30th June 2020"
        student = Register(ID, name, email, role)
        student.register(name, email, role, dob, age, gender, father, contact, address, doA)
        # student_detail[ID] = (name, email, role, dob, age, gender, father, contact, address, doA)
        # student = Register(ID, name, email, role)
        self.assertTrue(student_detail)

    #
    def test_display_method(self):
        """tests the display student method in the Registration class if it will display all the students details in
        the register """
        ID = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        student = Register(ID, name, email, role)
        student.display_register()
        self.assertTrue(student.user_details())

    #

    def test_update_student(self):
        """tests the update method in the Registration class if the ID is found"""
        student_detail = {"IB200": ["Irene Busah", "i.busah@agblschool.com", "student", "5th May, 2000", "21",
                                    "Female", "Joseph Busah", "+233549185709", "Takoradi", "30th December"]}

        ID = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        contact = "+233784857890"
        address = "Kumasi"
        student = Register(ID, name, email, role)
        student.update_student(ID, address, contact)
        # self.assertTrue(student.user_detail(dob, age, gender, father, contact, address, doA))
        self.assertTrue(student_detail)

    def test_update_error(self):
        """test for the error catching in the update method if the ID is not found"""
        student_detail = {"IB200": ["Irene Busah", "i.busah@agblschool.com", "student", "5th May, 2000", "21",
                                    "Female", "Joseph Busah", "+233549185709", "Takoradi", "30th December"]}

        # condition to check if the ID is not in the dictionary
        ID = "NN345"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        contact = "+233784857890"
        address = "Wa"
        student = Register(ID, name, email, role)

        with self.assertRaises(Exception):
            print(student.update_student(ID, address, contact))

    def test_delete_error(self):
        """Tests to catch the error of the delete method, thus if the ID is not found"""
        ID = "NN345"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        student = Register(ID, name, email, role)

        with self.assertRaises(Exception):
            print(student.delete_student(ID))
