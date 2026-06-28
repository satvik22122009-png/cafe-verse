from db import connect_db
import tkinter as tk

def show_menu():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM menu")
    items = cursor.fetchall()

    window = tk.Toplevel()
    window.title("CafeVerse Menu")
    window.geometry("400x350")

    heading = tk.Label(
        window,
        text="☕ CafeVerse Menu",
        font=("Arial", 18, "bold")
    )
    heading.pack(pady=10)

    for item in items:
        tk.Label(
            window,
            text=f"{item[0]}. {item[1]} - ₹{item[2]}",
            font=("Arial", 12)
        ).pack()

    conn.close()
    