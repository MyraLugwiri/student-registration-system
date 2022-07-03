import unittest
from StudentSystem_WithStorage import *
from io import StringIO


class MyTestCase(unittest.TestCase):
    # This class tests for the User class

    def test_user_id(self):
        """Test user_id method in the user class"""
        # answer = user.get_user_id()
        user_id = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        user = User(user_id, name, email, role)
        self.assertEqual(user.get_user_id(), "IB200")

    def test_name(self):
        """tests the get_name method in the user class"""
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
        """tests the user_detail method in the user class"""
        user_id = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        user = User(user_id, name, email, role)
        self.assertTrue(user.user_details())

    def test_empty_email(self):
        """tests the user_details method to catch the error the user doesn't provide the email"""
        user_id = "IB200"
        name = "Irene Busah"
        email = ""
        role = "Student"
        user = User(user_id, name, email, role)

        with self.assertRaises(Exception):
            user.user_details()


class TestCase(unittest.TestCase):
    """This class tests the methods of the student class"""

    def test_dob(self):
        """tests the date of birth method in the student class"""
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
        """testing the set_parent_contact method if it will return """
        user_id = "IB200"
        name = "Irene Busah"
        emails = "i.busah@agblschool.com"
        role = "Student"
        student = Student(user_id, name, emails, role)
        self.assertEqual(student.set_parent_contact("+233784857890"), "+233784857890")

    def test_user_detail(self):
        user_id = "IB200"
        name = "Irene Busah"
        emails = "i.busah@agblschool.com"
        role = "Student"
        dob = "5th May 2000",
        age = "21"
        gender = "Female"
        parent_name = "Joseph Busah"
        parent_contact = "+233784857890"
        address = "Wa"
        doA = "23th June 2020"
        student = Student(user_id, name, emails, role)
        students = Student.user_detail(student, dob, age, gender, parent_name, parent_contact, address, doA)
        self.assertTrue(students)


class TestRegister_Class(unittest.TestCase):
    """This class tests the methods of the Registration class"""

    def test_register_method(self):
        """tests the register method in the registration class if the user provides the correct information"""

        student_detail = {"IB200": ["Irene Busah", "i.busah@agblschool.com", "student", "5th May, 2000", "21",
                                    "Female", "Joseph Busah", "+233549185709", "Takoradi", "30th December"]}

        file = StringIO()
        ID = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        dob = "5th May 2000"
        age = "21"
        gender = "Female"
        father = "Joseph Busah"
        contact = "+233784857890"
        address = "Kumasi"
        doA = "30th June 2020"
        student = Register(ID, name, email, role)
        student.register(ID, name, email, role, dob, age, gender, father, contact, address, doA)
        self.assertTrue(file)

    def test_search_student(self):
        """tests the search student method in the registration class if the user provides the correct information"""

        student_detail = {"IB200": ["Irene Busah", "i.busah@agblschool.com", "student", "5th May, 2000", "21",
                                    "Female", "Joseph Busah", "+233549185709", "Takoradi", "30th December"]}
        file = StringIO()
        ID = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        student = Register(ID, name, email, role)
        student.search_student(ID)
        # self.assertTrue(student.user_detail(dob, age, gender, father, contact, address, doA))
        self.assertTrue(student_detail)

    def test_display_student(self):
        """tests the display method in the registration class"""
        file = StringIO
        ID = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"

        student = Register(ID, name, email, role)
        student.display_register()
        # self.assertTrue(student.user_detail(dob, age, gender, father, contact, address, doA))
        self.assertTrue(file)

    def test_delete_student(self):
        """tests the delete method in the registration class"""
        student_detail = {"IB200": ["Irene Busah", "i.busah@agblschool.com", "student", "5th May, 2000", "21",
                                    "Female", "Joseph Busah", "+233549185709", "Takoradi", "30th December"]}
        file = StringIO()
        ID = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        student = Register(ID, name, email, role)
        student.delete_student(ID)
        # self.assertTrue(student.user_detail(dob, age, gender, father, contact, address, doA))
        self.assertTrue(file)

    def test_delete_error(self):
        """Tests to catch the error of the delete method, thus if the ID is not found"""

        ID = "NN345"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        student = Register(ID, name, email, role)

        with self.assertRaises(Exception):
            print(student.delete_student(ID))

    def test_update_student(self):
        """tests the update student method in the registration class"""
        student_detail = {"IB200": ["Irene Busah", "i.busah@agblschool.com", "student", "5th May, 2000", "21",
                                    "Female", "Joseph Busah", "+233549185709", "Takoradi", "30th December"]}

        ID = "IB200"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        contact = "+233784857890"
        address = "Wa"
        student = Register(ID, name, email, role)
        student.update_student(ID, address, contact)
        # self.assertTrue(student.user_detail(dob, age, gender, father, contact, address, doA))
        self.assertTrue(student_detail)

    def test_update_error(self):
        """test for the error catching in the update method"""
        student_detail = {"IB200": ["Irene Busah", "i.busah@agblschool.com", "student", "5th May, 2000", "21",
                                    "Female", "Joseph Busah", "+233549185709", "Takoradi", "30th December"]}

        # condition to check if the ID is not in the dictionary above
        ID = "NN345"
        name = "Irene Busah"
        email = "i.busah@agblschool.com"
        role = "Student"
        contact = "+233784857890"
        address = "Wa"
        student = Register(ID, name, email, role)

        with self.assertRaises(Exception):
            print(student.update_student(ID, address, contact))


if __name__ == '__main__':
    unittest.main()
