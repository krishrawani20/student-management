from confugration import StudentStore
from utility import UI
from validator import Validator
from displayy import Display
from file_handle import FileHandler


class StudentPortal:

    def login(self):
        UI.header("Student Login")

        student_id = input("Student ID : ").strip()
        password = Validator.mask_password()

        record = self._find(student_id, password)

        if not record:
            UI.error("Invalid Student ID or Password.")
            UI.press_enter()
            return

        UI.success(f"Welcome, {record['full_name']}!")
        self._dashboard(record)

    def _find(self, student_id, password):
        for student in StudentStore.all():
            if (
                student["student_id"] == student_id
                and student["password"] == password
            ):
                return student
        return None

    def _dashboard(self, record):
        while True:
            UI.header(f"Student Dashboard - {record['student_id']}")

            print("1. View My Profile")
            print("2. Update My Details")
            print("3. View My Course & Fee")
            print("4. Check Registration Status")
            print("5. Logout")

            UI.separator()

            choice = input("Select Option : ").strip()

            if choice == "1":
                Display.profile(record)
                UI.press_enter()

            elif choice == "2":
                self._update(record)

            elif choice == "3":
                fee = int(record.get("fee", 0))

                UI.header("Course & Fee Information")
                print(f"Course         : {record['course']}")
                print(f"Annual Fee     : ₹{fee:,}")
                print(f"Per Semester   : ₹{fee//2:,}")
                print(f"Per Month      : ₹{fee//12:,}")
                UI.separator()
                UI.press_enter()

            elif choice == "4":
                UI.header("Registration Status")
                print(f"Student ID : {record['student_id']}")
                print(f"Name       : {record['full_name']}")
                print(f"Status     : {record['status']}")
                print(f"Reg. Date  : {record['reg_date']}")
                UI.separator()
                UI.press_enter()

            elif choice == "5":
                UI.info("Logged out successfully.")
                UI.press_enter()
                break

            else:
                UI.error("Invalid option.")
                UI.press_enter()

    def _update(self, record):

        UI.header("Update My Details")

        print("1. Mobile Number")
        print("2. Email Address")
        print("3. Address")
        print("4. Password")
        print("5. Back")

        UI.separator()

        choice = input("Select Option : ").strip()

        if choice == "1":

            while True:
                mobile = input("New Mobile : ").strip()

                if Validator.phone(mobile):
                    record["mobile"] = mobile
                    break

                UI.error("Invalid phone number.")

        elif choice == "2":

            while True:
                email = input("New Email : ").strip()

                if Validator.email(email):
                    record["email"] = email
                    break

                UI.error("Invalid email address.")

        elif choice == "3":

            record["address"] = (
                input("New Address : ").strip()
                or record["address"]
            )

        elif choice == "4":

            while True:

                old = Validator.mask_password("Current Password : ")

                if old != record["password"]:
                    UI.error("Incorrect current password.")
                    continue

                new1 = Validator.mask_password("New Password : ")
                new2 = Validator.mask_password("Confirm Password : ")

                if len(new1) < 6:
                    UI.error("Password must be at least 6 characters.")
                    continue

                if new1 != new2:
                    UI.error("Passwords do not match.")
                    continue

                record["password"] = new1
                break

        elif choice == "5":
            return

        else:
            UI.error("Invalid option.")
            UI.press_enter()
            return

        FileHandler.save()
        UI.success("Details updated successfully.")
        UI.press_enter()