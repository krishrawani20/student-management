
import datetime
from confugration import Config
from utility import UI


class WelcomeScreen:
    """Displays the application startup banner."""

    @staticmethod
    def show():
        UI.clear()
        UI.separator("=")

        print()
        print("   ============================================================")
        print("   ||                                                        ||")
        print("   ||       UNIVERSITY STUDENT REGISTRATION SYSTEM           ||")
        print("   ||                                                        ||")
        print("   ============================================================")
        print()

        UI.separator("=")
        print(f"  Data File : {Config.DATA_FILE}")
        print(f"  Date/Time : {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
        UI.separator("=")

        UI.press_enter()