

from utility import UI
from registration import RegistrationService
from studentportal import StudentPortal
from adminpanel import AdminPanel
from displayy import Display
from file_handle import FileHandler
from welcome import WelcomeScreen


class MainMenu:

    def __init__(self):
        self.registration = RegistrationService()
        self.student_portal = StudentPortal()
        self.admin_panel = AdminPanel()

    def run(self):
       
        FileHandler.load()

        
        WelcomeScreen.show()

        while True:
            UI.clear()
            UI.header("University Registration System")

            print("1. Student Registration")
            print("2. Student Login")
            print("3. Admin Login")
            print("4. Display All Students")
            print("5. Search Student")
            print("6. Course & Fee Information")
            print("7. Exit")

            UI.separator()

            choice = input("Select Option : ").strip()

            if choice == "1":
                self.registration.register()

            elif choice == "2":
                self.student_portal.login()

            elif choice == "3":
                self.admin_panel.login()

            elif choice == "4":
                Display.all_students()
                UI.press_enter()

            elif choice == "5":
                self.admin_panel._search()

            elif choice == "6":
                Display.fee_information()

            elif choice == "7":
                UI.separator()
                print("\nThank you for using the University Registration System.")
                print("Goodbye!")
                UI.separator()
                break

            else:
                UI.error("Invalid option. Please select a number between 1 and 7.")
                UI.press_enter()


if __name__ == "__main__":
    MainMenu().run()         