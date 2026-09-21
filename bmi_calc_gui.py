import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

root = tk.Tk()
root.title("BMI Calculator")

name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

weight_label = tk.Label(root, text="Weight (kg):")
weight_entry = tk.Entry(root)

height_label = tk.Label(root, text="Height (m):")
height_entry = tk.Entry(root)

calculate_button = tk.Button(root, text="calculate")
result_label = tk.Label(root, text="")

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

weight_label.grid(row=1, column=0)
weight_entry.grid(row=1, column=1)

height_label.grid(row=2, column=0)
height_entry.grid(row=2, column=1)

calculate_button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)

def calculate_bmi():
    name = name_entry.get()
    weight = weight_entry.get()
    height = height_entry.get()

    try:
        weight = float(weight)
        height = float(height)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numeric values for weight and height.")
        return

    if weight <= 0 or height <= 0:
        messagebox.showerror("Invalid Input", "Weight and height must be positive values.")
        return

    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "underweight"
        color = "orange"
    elif bmi <= 24.9:
        category = "normal weight"
        color = "green"
    elif bmi <= 29.9:
        category = "overweight"
        color = "yellow"
    else:
        category = "obese"
        color = "red"

    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    try:
        date = datetime.now().isoformat()
        cursor.execute('''CREATE TABLE IF NOT EXISTS bmi_records
                         (name TEXT, weight REAL, height REAL, bmi REAL, category TEXT, date TEXT)''')
        cursor.execute(
            "INSERT INTO bmi_records VALUES (?, ?, ?, ?, ?, ?)",
            (name, weight, height, bmi, category, date),
        )
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred while saving data: {e}")
    finally:
        conn.close()

    result_label.config(text=f"Your BMI is: {round(bmi, 2)} and you are classified as {category}.", fg=color)


calculate_button.config(command=calculate_bmi)

def view_bmi_graph():
    name = name_entry.get()

    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT date, bmi FROM bmi_records WHERE name = ? ORDER BY date", (name,))
        records = cursor.fetchall()

        if not records:
            messagebox.showinfo("No Data", "No BMI records found to display.")
            return

        dates = [datetime.fromisoformat(record[0]) for record in records]
        bmis = [record[1] for record in records]

        import matplotlib.pyplot as plt

        plt.figure(figsize=(10, 5))
        plt.plot(dates, bmis, marker='o')
        plt.title("BMI Over Time")
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid()
        plt.show()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred while retrieving data: {e}")
    finally:
        conn.close()


graph_button = tk.Button(root, text="View BMI Graph", command=view_bmi_graph)
graph_button.grid(row=5, column=0, columnspan=2)

root.mainloop()