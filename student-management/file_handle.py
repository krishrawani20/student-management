import csv
import os
import datetime

from confugration import Config, StudentStore
from utility import UI


class FileHandler:

    FIELDS = [
        "student_id",
        "full_name",
        "age",
        "gender",
        "dob",
        "mobile",
        "email",
        "address",
        "course",
        "fee",
        "qualification",
        "password",
        "status",
        "reg_date"
    ]

    @staticmethod
    def save():
        with open(Config.DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FileHandler.FIELDS)
            writer.writeheader()

            if StudentStore.count():
                writer.writerows(StudentStore.all())

    @staticmethod
    def load():
        if not os.path.exists(Config.DATA_FILE):
            return

        with open(Config.DATA_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            records = [dict(row) for row in reader]

        for s in records:
            try:
                s["fee"] = int(s["fee"])
            except (ValueError, KeyError):
                s["fee"] = 0

        StudentStore.load_from(records)

    @staticmethod
    def export():
        if not StudentStore.count():
            UI.error("No data to export.")
            UI.press_enter()
            return

        os.makedirs("exports", exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(
            "exports",
            f"students_export_{timestamp}.csv"
        )

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FileHandler.FIELDS)
            writer.writeheader()
            writer.writerows(StudentStore.all())

        UI.success(f"Data exported successfully to '{filename}'.")
        UI.press_enter()