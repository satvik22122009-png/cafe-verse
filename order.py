import tkinter as tk
from tkinter import ttk, messagebox
from db import connect_db


def open_order_window():

    window = tk.Toplevel()
    window.title("Place Order")
    window.geometry("450x350")

    tk.Label(window, text="Place Your Order", font=("Arial", 18, "bold")).pack(pady=15)

    tk.Label(window, text="Customer Name").pack()
    name_entry = tk.Entry(window, width=30)
    name_entry.pack(pady=5)

    tk.Label(window, text="Phone Number").pack()
    phone_entry = tk.Entry(window, width=30)
    phone_entry.pack(pady=5)

    tk.Label(window, text="Select Item").pack()

    items = [
        "Pizza",
        "Burger",
        "Coffee",
        "Cold Drink",
        "French Fries",
        "Pasta",
        "Sandwich",
        "Mojito"
    ]

    combo = ttk.Combobox(window, values=items, state="readonly")
    combo.pack(pady=5)
    combo.current(0)

    tk.Label(window, text="Quantity").pack()
    qty = tk.Spinbox(window, from_=1, to=20, width=10)
    qty.pack(pady=5)

    def place_order():

        name = name_entry.get()
        phone = phone_entry.get()
        item = combo.get()
        quantity = int(qty.get())

        conn = connect_db()
        cursor = conn.cursor()

        # Save Customer
        cursor.execute(
            "INSERT INTO customers (customer_name, phone) VALUES (%s,%s)",
            (name, phone)
        )

        customer_id = cursor.lastrowid

        # Get Item Price
        cursor.execute(
            "SELECT price FROM items WHERE item_name = %s",
            (item,)
        )

        result = cursor.fetchone()
        if not result:
            messagebox.showerror("Error", "Item not found!")
            conn.close()
            return

        price = float(result[0])
        total = price * quantity

        # Save Order
        cursor.execute(
            "INSERT INTO orders (customer_id, total_amount) VALUES (%s,%s)",
            (customer_id, total)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Order Saved Successfully!")

    tk.Button(
        window,
        text="Place Order",
        width=20,
        command=place_order
    ).pack(pady=20)