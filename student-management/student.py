
import datetime


class Student:

    def __init__(
        self,
        student_id,
        full_name,
        age,
        gender,
        dob,
        mobile,
        email,
        address,
        course,
        fee,
        qualification,
        password,
        status="Registered",
        reg_date=None,
    ):

        self.student_id = student_id
        self.full_name = full_name
        self.age = str(age)
        self.gender = gender
        self.dob = dob
        self.mobile = mobile
        self.email = email
        self.address = address
        self.course = course

        try:
            self.fee = int(fee)
        except (ValueError, TypeError):
            self.fee = 0

        self.qualification = qualification
        self.password = password
        self.status = status
        self.reg_date = (
            reg_date
            if reg_date
            else datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        )

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "age": self.age,
            "gender": self.gender,
            "dob": self.dob,
            "mobile": self.mobile,
            "email": self.email,
            "address": self.address,
            "course": self.course,
            "fee": self.fee,
            "qualification": self.qualification,
            "password": self.password,
            "status": self.status,
            "reg_date": self.reg_date,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data.get("student_id", ""),
            full_name=data.get("full_name", ""),
            age=data.get("age", ""),
            gender=data.get("gender", ""),
            dob=data.get("dob", ""),
            mobile=data.get("mobile", ""),
            email=data.get("email", ""),
            address=data.get("address", ""),
            course=data.get("course", ""),
            fee=data.get("fee", 0),
            qualification=data.get("qualification", ""),
            password=data.get("password", ""),
            status=data.get("status", "Registered"),
            reg_date=data.get("reg_date"),
        )

    def __str__(self):
        return f"Student(ID={self.student_id}, Name={self.full_name}, Course={self.course})"

    def __repr__(self):
        return self.__str__()