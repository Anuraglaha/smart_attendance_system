import sqlite3
from datetime import datetime


def markAttendanceDB(name):

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # Ensure table exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL
    )
    """)

    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")

    # Checking if already marked today
    cursor.execute(
        "SELECT * FROM attendance WHERE name=? AND date=?",
        (name, date)
    )

    result = cursor.fetchone()

    if result is None:
        # Insert only if not present
        cursor.execute(
            "INSERT INTO attendance (name, date, time) VALUES (?, ?, ?)",
            (name, date, time)
        )

        conn.commit()
        print(f"{name} marked present in DB")

    else:
        print(f"{name} already marked today!!")

    conn.close()


#testing the code
#markAttendanceDB("ANURAG")
#markAttendanceDB("ANURAG")