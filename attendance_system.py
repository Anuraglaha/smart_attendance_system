import csv
from datetime import datetime


def markAttendance(name):
    file_path = "attendance.csv"

    try:
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            names = [row[0] for row in reader]
    except FileNotFoundError:
        names = []

    # If name not already present
    if name not in names:
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")

        with open(file_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, date, time])

        print(f"{name} marked present✅")

