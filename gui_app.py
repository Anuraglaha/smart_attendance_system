import customtkinter as ctk
from recognize_faces import run_attendance
import threading
running = False
# ---------- Theme ----------
ctk.set_appearance_mode("dark")     # Dark / Light / System
ctk.set_default_color_theme("blue") # Theme color


# ---------- Main Window ----------
app = ctk.CTk()
app.title("Smart Attendance System")
app.geometry("500x400")  # Width x Height

# ---------- Title Label ----------
title_label = ctk.CTkLabel(
    app,
    text="SMART ATTENDANCE SYSTEM",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=30)

# ---------- Button Functions ----------
def start_attendance():
    global running

    if not running:
        running = True
        status_label.configure(text="Status: Running")

        def task():

            def update_last(name):
                last_marked_label.configure(
                    text=f"Last Marked: {name}"
                )

            run_attendance(
                lambda: running,
                update_last
            )

            status_label.configure(text="Status: Stopped")

        threading.Thread(target=task, daemon=True).start()

'''
def start_attendance():
    global running

    if not running:
        running = True
        status_label.configure(text="Status: Running")

        run_attendance(lambda: running)

        status_label.configure(text="Status: Stopped")
'''

def stop_attendance():
    global running

    running = False
    status_label.configure(text="Status: Stopping...")

# ---------- Start Button ----------
start_button = ctk.CTkButton(
    app,
    text="Start Attendance",
    font=("Arial", 16),
    command=start_attendance
)

start_button.pack(pady=10)


# ---------- Stop Button ----------
stop_button = ctk.CTkButton(
    app,
    text="Stop",
    font=("Arial", 16),
    fg_color="red",
    hover_color="darkred",
    command=stop_attendance
)

stop_button.pack(pady=10)

# ---------- Status Label ----------
status_label = ctk.CTkLabel(
    app,
    text="Status: Ready",
    font=("Arial", 16)
)

status_label.pack(pady=20)


# ---------- Last Marked Label ----------
last_marked_label = ctk.CTkLabel(
    app,
    text="Last Marked: —",
    font=("Arial", 14)
)

last_marked_label.pack()

# ---------- Run App ----------
app.mainloop()