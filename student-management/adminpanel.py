from confugration import Config, StudentStore
from utility import UI
from validator import Validator
from displayy import Display
from file_handle import FileHandler
from registration import RegistrationService


class AdminPanel:

    def login(self):
        UI.header("Admin Login")

        username = input("Username : ").strip()
        password = Validator.mask_password("Password : ")

        if username != Config.ADMIN_USERNAME or password != Config.ADMIN_PASSWORD:
            UI.error("Invalid Username or Password.")
            UI.press_enter()
            return

        UI.success("Admin logged in successfully.")
        UI.press_enter()
        self._panel()

    def _panel(self):
        while True:
            UI.header("Admin Panel")

            print("1. View All Students")
            print("2. Search Student")
            print("3. Add New Student")
            print("4. Update Student Record")
            print("5. Delete Student Record")
            print("6. Total Registered Students")
            print("7. Sort Students by Name")
            print("8. Display Course & Fee Table")
            print("9. Export Student List to CSV")
            print("10. Logout")

            UI.separator()

            choice = input("Select Option : ").strip()

            if choice == "1":
                Display.all_students()
                UI.press_enter()

            elif choice == "2":
                self._search()

            elif choice == "3":
                RegistrationService().register()

            elif choice == "4":
                self._update()

            elif choice == "5":
                self._delete()

            elif choice == "6":
                self._count()

            elif choice == "7":
                self._sort()

            elif choice == "8":
                Display.courses()
                UI.press_enter()

            elif choice == "9":
                FileHandler.export()

            elif choice == "10":
                UI.info("Admin logged out successfully.")
                UI.press_enter()
                break

            else:
                UI.error("Invalid option. Please try again.")
                UI.press_enter()


    def _search(self):
        UI.header("Search Student")

        print("1. Search by Student ID")
        print("2. Search by Name")
        print("3. Search by Course")

        UI.separator()

        choice = input("Select Option : ").strip()

        results = []

        if choice == "1":
            sid = input("Enter Student ID : ").strip()

            results = [
                s for s in StudentStore.all()
                if s["student_id"].lower() == sid.lower()
            ]

        elif choice == "2":
            name = input("Enter Student Name : ").strip().lower()

            results = [
                s for s in StudentStore.all()
                if name in s["full_name"].lower()
            ]

        elif choice == "3":
            course = input("Enter Course Name : ").strip().lower()

            results = [
                s for s in StudentStore.all()
                if course in s["course"].lower()
            ]

        else:
            UI.error("Invalid option.")
            UI.press_enter()
            return

        if not results:
            UI.error("No matching student found.")
            UI.press_enter()
            return

        UI.success(f"{len(results)} record(s) found.\n")

        for student in results:
            Display.profile(student)

        UI.press_enter()


    def _update(self):
        UI.header("Update Student Record")

        sid = input("Enter Student ID : ").strip()

        target = next(
            (s for s in StudentStore.all()
             if s["student_id"] == sid),
            None
        )

        if target is None:
            UI.error("Student not found.")
            UI.press_enter()
            return

        print(f"\nStudent : {target['full_name']}")
        UI.separator()

        print("1. Full Name")
        print("2. Age")
        print("3. Mobile Number")
        print("4. Email Address")
        print("5. Address")
        print("6. Course")
        print("7. Status")
        print("8. Back")

        UI.separator()

        choice = input("Select Field : ").strip()

        if choice == "1":

            name = input("New Full Name : ").strip()

            if Validator.name(name):
                target["full_name"] = name
            else:
                UI.error("Invalid name.")
                UI.press_enter()
                return

        elif choice == "2":

            age = input("New Age : ").strip()

            if Validator.age(age):
                target["age"] = str(int(age))
            else:
                UI.error("Age must be between 15 and 60.")
                UI.press_enter()
                return

        elif choice == "3":

            mobile = input("New Mobile Number : ").strip()

            if Validator.phone(mobile):
                target["mobile"] = mobile
            else:
                UI.error("Invalid mobile number.")
                UI.press_enter()
                return

        elif choice == "4":

            email = input("New Email Address : ").strip()

            if Validator.email(email):
                target["email"] = email
            else:
                UI.error("Invalid email address.")
                UI.press_enter()
                return

        elif choice == "5":

            address = input("New Address : ").strip()

            if address:
                target["address"] = address

        elif choice == "6":

            Display.courses()

            course = input("Select Course Number : ").strip()

            if course in Config.courses:
                target["course"] = Config.courses[course]["name"]
                target["fee"] = Config.courses[course]["fee"]
            else:
                UI.error("Invalid course.")
                UI.press_enter()
                return

        elif choice == "7":

            status = input(
                "Status (Registered/Pending/Cancelled) : "
            ).strip().capitalize()

            if Validator.status(status):
                target["status"] = status
            else:
                UI.error("Invalid status.")
                UI.press_enter()
                return

        elif choice == "8":
            return

        else:
            UI.error("Invalid option.")
            UI.press_enter()
            return

        FileHandler.save()

        UI.success("Student record updated successfully.")
        UI.press_enter()    


    def _delete(self):
        UI.header("Delete Student Record")

        sid = input("Enter Student ID : ").strip()

        index = -1

        for i, student in enumerate(StudentStore.all()):
            if student["student_id"] == sid:
                index = i
                break

        if index == -1:
            UI.error("Student not found.")
            UI.press_enter()
            return

        student = StudentStore.all()[index]

        print(f"\nStudent Name : {student['full_name']}")
        print(f"Course       : {student['course']}")
        print(f"Status       : {student['status']}")

        UI.separator()

        confirm = input(
            "Are you sure you want to delete this student? (yes/no): "
        ).strip().lower()

        if confirm == "yes":
            StudentStore.remove(index)
            FileHandler.save()

            UI.success("Student record deleted successfully.")
        else:
            UI.info("Deletion cancelled.")

        UI.press_enter()


    def _count(self):
        UI.header("Total Registered Students")

        total = StudentStore.count()

        print(f"\nTotal Students : {total}")

        UI.separator()
        UI.press_enter()


    def _sort(self):
        UI.header("Sort Students")

        StudentStore.sort_by_name()
        FileHandler.save()

        UI.success("Students sorted by name successfully.")

        UI.press_enter()        