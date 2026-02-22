====SMART ATTENDANCE SYSTEM (FACE RECOGNITION)====

A desktop-based attendance system that automatically records presence using real-time face recognition.
This application captures faces through a webcam, identifies registered individuals, and logs attendance with timestamps in a local database. It is packaged as a standalone Windows executable and does not require Python to be installed on the target system.

---FEATURES---

Real-time face detection and recognition
Automatic attendance marking with date and time
Duplicate prevention (one entry per person per day)
Local SQLite database storage
Simple graphical user interface
Start/Stop controls for camera operation
Standalone Windows executable (no setup required)

---TECHNOLOGIES USED---

Python
OpenCV
face_recognition (dlib-based)
SQLite
CustomTkinter
PyInstaller

---RELEASE---

Download the latest version from the Releases section:
>> Windows executable package included

---How to Use---
1. Prepare Face Images

Place images of registered individuals inside the images folder.

--!! Naming format !!--
    Name_<number>.jpg
Examples:
Anurag_1.jpg
Anurag_2.png
Her_1.jpeg

Supported formats:
.jpg  .jpeg  .png

2. Run the Application
Launch the executable:
  gui_app.exe
Click Start Attendance and look at the camera.
Recognized individuals will be marked automatically.

3. Stop the System
You can stop recognition by:
Clicking the Stop button
Pressing the ESC key

---ATTENDANCE STORAGE---
Attendance records are stored locally in:
attendance.db

Each entry includes:
Name
Date
Time

---PROJECT STRUCTURE---
Smart Attendance/
|__ gui_app.exe
|__images/
|__attendance.db

---NOTES---
Ensure the webcam is connected and accessible
Images should clearly show the person's face
Performance may vary depending on lighting conditions

---CURRENT STATUS---
Initial stable release (v1.0).
Further improvements and features are planned.

---AUTHOR---
Developed by Anurag Laha
