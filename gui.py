from order import open_order_window
from menu import show_menu
import tkinter as tk
from tkinter import messagebox

def start_app():
    root = tk.Tk()

    root.title("CafeVerse")
    root.geometry("700x500")
    root.resizable(False, False)

    title = tk.Label(
        root,
        text="☕ CafeVerse",
        font=("Arial", 22, "bold")
    )
    title.pack(pady=20)
    tk.Label(
    root,
    text="Cafe & Restaurant Management System",
    font=("Arial", 11)
).pack()

    tk.Button(
    root,
    text="View Menu",
    width=20,
    height=2,
    command=show_menu
).pack(pady=10)

    tk.Button(
    root,
    text="Place Order",
    width=20,
    height=2,
    command=open_order_window
).pack(pady=10)

    tk.Button(root, text="View Orders", width=20, height=2).pack(pady=10)

    tk.Button(root, text="Admin", width=20, height=2).pack(pady=10)

    tk.Button(root, text="Exit", width=20, height=2,
              command=root.destroy).pack(pady=20)

    root.mainloop()

