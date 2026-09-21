class Config:
    
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "aalukaaju123"
    DATA_FILE = "unv.csv"

    courses = {
        "1" : {"name": "Diploma Computer Science", "duration": "3 years", "fee": 45000},
        "2" : {"name": "Diploma Electrial Engeenering", "duration": "3 years", "fee": 45000},
        "3" : {"name": "BCA", "duration": "3 years", "fee": 450000},
        "4" : {"name": "MCA", "duration": "3 years", "fee": 450000},
        "5" : {"name": "B.Tech Computer Science", "duration": "3 years", "fee": 50000},
        "6" : {"name": "B.com", "duration": "3 years", "fee": 45000},
        "7" : {"name": "B.Sc Mathemmatics", "duration": "3 years", "fee": 45000},
        "8" : {"name": "B.Sc IT", "duration": "3 years", "fee": 350000},
    }

class StudentStore:
    _students = []

    @classmethod
    def all(cls):
        return cls._students.copy()
    
    @classmethod
    def add(cls, student_dict):
        cls._students.append(student_dict)

    @classmethod
    def remove(cls, index):
        if 0 <= index < len(cls._students):
            cls._students.pop(index)
            return True
        return False

    @classmethod
    def count(cls):
        return len(cls._students)
    
    @classmethod
    def sort_by_name(cls):
        cls._students.sort(key = lambda s: s["full_name"].lower())

    @classmethod
    def load_from(cls, records):
        cls._students = list(records)