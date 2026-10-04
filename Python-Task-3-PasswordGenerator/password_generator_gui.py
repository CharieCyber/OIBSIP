import tkinter as tk 
from tkinter import ttk, messagebox
import secrets
import string



root = tk.Tk()
root.title("Password Generator")

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()
ambiguous_var = tk.BooleanVar()


length_label = tk.Label(root, text="Password Length: ")
length_spinbox = tk.Spinbox(root, from_=8, to=64)

upper_check = tk.Checkbutton(root, text="Uppercase Letters", variable=upper_var)
lower_check = tk.Checkbutton(root, text="Lowercase Letters", variable=lower_var)
digits_check = tk.Checkbutton(root, text="Numbers", variable=digits_var)
symbols_check = tk.Checkbutton(root, text="Symbols", variable=symbols_var)
ambiguous_check = tk.Checkbutton(root, text="Exclude ambiguous characters (0, O, l, 1)", variable=ambiguous_var)

generate_button = tk.Button(root, text="Generate")
result_label = tk.Label(root, text="")
copy_button = tk.Button(root, text="Copy to Clipboard")
history_listbox = tk.Listbox(root, height=5, width=40)

length_label.grid(row=0, column=0)
length_spinbox.grid(row=0, column=1)
upper_check.grid(row=1, column=0, columnspan=2 )
lower_check.grid(row=2, column=0, columnspan=2 )
digits_check.grid(row=3, column=0, columnspan=2 )
symbols_check.grid(row=4, column=0, columnspan=2 )
ambiguous_check.grid(row=5, column=0, columnspan=2)
copy_button.grid(row=8, column=0, columnspan=2)
generate_button.grid(row=6, column=0, columnspan=2)
result_label.grid(row=7, column=0, columnspan=2)
history_listbox.grid(row=9, column=0, columnspan=2)



def calculate_strength(password, types_used):
    if len(password) >= 12 and types_used >= 3:
        return "Strong", "green"
    elif len(password) >= 8 and types_used >= 2:
        return "Medium", "orange"
    else:
        return "Weak", "red"

password_history = []
current_password = ""  

def generate_password():
    global current_password
    try:
        length = int(length_spinbox.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")
        return

    selected_pools = []
    if upper_var.get():
        selected_pools.append(string.ascii_uppercase)
    if lower_var.get():
        selected_pools.append(string.ascii_lowercase)
    if digits_var.get():
        selected_pools.append(string.digits)
    if symbols_var.get():
        selected_pools.append(string.punctuation)

    selected_count = len(selected_pools)
    if selected_count < 2:
        messagebox.showerror("Invalid Selection", "Please select at least 2 character types.")
        return

    if ambiguous_var.get():
        ambiguous_chars = "0OIl1"
        selected_pools = [
            ''.join(ch for ch in pool if ch not in ambiguous_chars)
            for pool in selected_pools
        ]
        if any(not pool for pool in selected_pools):
            messagebox.showerror("Invalid Selection", "No valid characters remain after excluding ambiguous ones.")
            return

    if length < selected_count :
        messagebox.showerror("Invalid Length", f"Password length must be at least {selected_count} characters.")
        return

    guaranteed_chars = [secrets.choice(pool) for pool in selected_pools]
    character_pool = ''.join(selected_pools)
    remaining_length = length - len(guaranteed_chars)
    remaining_chars = [secrets.choice(character_pool) for _ in range(remaining_length)]
    all_chars = guaranteed_chars + remaining_chars
    secrets.SystemRandom().shuffle(all_chars)
    password = ''.join(all_chars)
    current_password = password

    password_history.insert(0, password)
    password_history[:] = password_history[:5]
    history_listbox.delete(0, tk.END)
    for pwd in password_history:
        history_listbox.insert(tk.END, pwd)

        
    strength_text, strength_color = calculate_strength(password, selected_count)
    result_label.config(text=f"{password} ({strength_text})", fg=strength_color)


def copy_to_clipboard():
    print(f"Copying: '{current_password}'")
    root.clipboard_clear()
    root.clipboard_append(current_password)
    root.update()

generate_button.config(command=generate_password)
copy_button.config(command=copy_to_clipboard)    

root.mainloop()