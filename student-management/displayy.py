from confugration import Config, StudentStore
from utility import UI


class Display:

    @staticmethod
    def courses():
        UI.header("Available Courses & Fees")
        print(f"{'No.':<5} {'Course Name':<40} {'Annual Fee (INR)':>15}")
        UI.separator("-")

        for key, info in Config.courses.items():
            print(f"{key:<5} {info['name']:<40} ₹{info['fee']:>10,}")

        UI.separator("-")

    @staticmethod
    def receipt(student):
        UI.separator("*")
        print("UNIVERSITY REGISTRATION RECEIPT".center(UI.WIDTH))
        UI.separator("*")

        fee = int(student.get("fee", 0))

        print(f"Student ID     : {student['student_id']}")
        print(f"Full Name      : {student['full_name']}")
        print(f"Course         : {student['course']}")
        print(f"Annual Fee     : ₹{fee:,}")
        print(f"Status         : {student['status']}")
        print(f"Register Date  : {student['reg_date']}")

        UI.separator("*")

    @staticmethod
    def profile(student):
        UI.header("Student Profile")

        fee = int(student.get("fee", 0))

        print(f"Student ID     : {student['student_id']}")
        print(f"Full Name      : {student['full_name']}")
        print(f"Age            : {student['age']}")
        print(f"Gender         : {student['gender']}")
        print(f"Date of Birth  : {student['dob']}")
        print(f"Mobile         : {student['mobile']}")
        print(f"Email          : {student['email']}")
        print(f"Address        : {student['address']}")
        print(f"Course         : {student['course']}")
        print(f"Annual Fee     : ₹{fee:,}")
        print(f"Qualification  : {student['qualification']}")
        print(f"Status         : {student['status']}")
        print(f"Register Date  : {student['reg_date']}")

        UI.separator()

    @staticmethod
    def all_students():
        UI.header(f"All Registered Students (Total: {StudentStore.count()})")

        if StudentStore.count() == 0:
            UI.info("No students registered yet.")
            UI.separator()
            return

        print(f"{'ID':<16} {'Name':<22} {'Course':<35} {'Status'}")
        UI.separator("-")

        for s in StudentStore.all():
            course = s["course"]
            if len(course) > 35:
                course = course[:32] + "..."

            print(
                f"{s['student_id']:<16}"
                f"{s['full_name']:<22}"
                f"{course:<35}"
                f"{s['status']}"
            )

        UI.separator()

    @staticmethod
    def fee_information():
        Display.courses()

        choice = input("Enter course number (Press ENTER to skip): ").strip()

        if choice in Config.courses:
            info = Config.courses[choice]

            print(f"\nCourse        : {info['name']}")
            print(f"Annual Fee    : ₹{info['fee']:,}")
            print(f"Per Semester  : ₹{info['fee']//2:,}")
            print(f"Per Month     : ₹{info['fee']//12:,}")
        else:
            UI.error("Invalid course number.")

        UI.press_enter()