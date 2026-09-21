import os
class UI:
    WIDTH = 62

    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def press_enter():
        input("\n press ENTER to continue..")

    @staticmethod
    def separator(char = "=", width = 62):
        print(char * width)


    @staticmethod
    def header(title):
        UI.separator()
        print(f"  {title.upper():^58}")
        UI.separator()

    @staticmethod
    def success(msg):
        print(f"\n[SUCCESS] {msg}")

    @staticmethod
    def error(msg):
        print(f"\n[ERROR] {msg}")

    @staticmethod
    def info(msg):
        print(f"\n[INFO] {msg}")

    @staticmethod
    def box(msg):
        UI.separator("-")
        print(msg.center(UI.WIDTH))
        UI.separator("-")