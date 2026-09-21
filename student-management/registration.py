from confugration import Config, StudentStore
from utility import UI
from validator import Validator
from displayy import Display
from file_handle import FileHandler
from student import Student


class RegistrationService:

    def register(self):
        UI.header("Student Registration")

        full_name = self._input_name()
        age = self._input_age()
        gender = self._input_gender()
        dob = self._input_dob()
        mobile = self._input_mobile()
        email = self._input_email()
        address = input("Address                 : ").strip() or "N/A"
        course, fee = self._input_course()
        qualification = input("Previous Qualification  : ").strip() or "N/A"
        password = self._input_password()

        student = Student(
            student_id=Validator.generate_student_id(StudentStore.all()),
            full_name=full_name,
            age=age,
            gender=gender,
            dob=dob,
            mobile=mobile,
            email=email,
            address=address,
            course=course,
            fee=fee,
            qualification=qualification,
            password=password,
        )

        StudentStore.add(student.to_dict())
        FileHandler.save()

        UI.success("Registration Successful!")
        Display.receipt(student.to_dict())
        UI.press_enter()

    def _input_name(self):
        while True:
            val = input("Full Name               : ").strip()
            if Validator.name(val):
                return val
            UI.error("Name must contain only letters and be at least 3 characters.")

    def _input_age(self):
        while True:
            val = input("Age                     : ").strip()
            if Validator.age(val):
                return int(val)
            UI.error("Age must be between 15 and 60.")

    def _input_gender(self):
        while True:
            val = input("Gender (M/F/O)          : ").strip().upper()
            if Validator.gender(val):
                return val
            UI.error("Enter M, F or O.")

    def _input_dob(self):
        while True:
            val = input("Date of Birth (DD/MM/YYYY): ").strip()
            if Validator.dob(val):
                return val
            UI.error("Invalid date. Use DD/MM/YYYY.")

    def _input_mobile(self):
        while True:
            val = input("Mobile Number           : ").strip()
            if Validator.phone(val):
                return val
            UI.error("Enter a valid 10-digit Indian mobile number.")

    def _input_email(self):
        while True:
            val = input("Email ID                : ").strip()
            if Validator.email(val):
                return val
            UI.error("Invalid email address.")

    def _input_course(self):
        Display.courses()

        while True:
            choice = input("Select Course Number    : ").strip()

            if choice in Config.courses:
                return (
                    Config.courses[choice]["name"],
                    Config.courses[choice]["fee"],
                )

            UI.error("Please select a valid course number.")

    def _input_password(self):
        while True:
            pw = Validator.mask_password("Create Password (min 6): ")
            cpw = Validator.mask_password("Confirm Password       : ")

            if len(pw) < 6:
                UI.error("Password must be at least 6 characters.")
                continue

            if pw != cpw:
                UI.error("Passwords do not match.")
                continue

            return pw