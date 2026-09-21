import re
import datetime

class Validator:

    @staticmethod
    def generate_student_id(existing_students):
        year = datetime.datetime.now().year
        existing_ids = [s.get("student_id") for s in existing_students]
        seq = 1
        while True:
            new_id = f"UNI-{year}-{seq:04d}"
            if new_id not in existing_ids:
                return new_id
            seq += 1

    @staticmethod
    def email(value):
        return bool(re.fullmatch(r'[\w\.-]+@[\w\.-]+\.\w{2,}', value))
    
    @staticmethod
    def phone(value):
        cleaned = re.sub(r'\D', '', value)

        if len(cleaned) == 12 and cleaned.startswith("91"):
            cleaned = cleaned[2:]

        return bool(re.fullmatch(r'[6-9]\d{9}', cleaned))
    
    @staticmethod
    def dob(dob_str):
        try:
            dob = datetime.datetime.strptime(dob_str, "%d/%m/%Y")
            today = datetime.datetime.now()

            age = (today - dob).days // 365

            if 15 <= age <= 60:
                return dob
            return None

        except ValueError:
            return None
        
    @staticmethod
    def name(value):
        value = value.strip()
        return bool(re.fullmatch(r"[A-Za-z ]{3,50}", value))
    
    @staticmethod
    def age(value):
        try:
            return 15 <= int(value) <= 60
        except ValueError:
            return False
        
    @staticmethod
    def gender(value):
        return value.strip().upper() in ("M", "F", "O")
    
    @staticmethod
    def status(value):
        return value.strip().capitalize() in ("Registered", "Pending", "Cancelled")
    
    @staticmethod
    def mask_password(passw = " Enter Password"):
        try:
            import getpass
            return getpass.getpass(passw)
        except Exception:
            return input(passw)