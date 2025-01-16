import tkinter as tk
import ttkbootstrap as ttk
import math 

def append_to_entry(value):
    """Appends the clicked button value to the entry field."""
    current = entry_var.get()
    entry_var.set(current + value)

def clear_entry():
    """Clears the entry field."""
    entry_var.set("")

def calculate_result():
    """Evaluates the expression in the entry field."""
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except Exception:
        entry_var.set("Error")

def append_pi():
    """Appends the value of pi to the entry field."""
    current = entry_var.get()
    entry_var.set(current + str(math.pi))

# Window setup
window = ttk.Window()
window.title("Calculator")
window.geometry('600x800') 
window.configure(bg="#4A235A")

# Entry field
entry_var = tk.StringVar()
entry = ttk.Entry(window, font=("comic-sans", 32), justify="right", textvariable=entry_var)
entry.pack(fill="x", padx=10, pady=20)  

# Button frame
button_frame = ttk.Frame(window)
button_frame.pack(pady=10)

# Button layout
buttons = [
    ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('%', 4, 0), ('0', 4, 1), ('.', 4, 2), ('=', 4, 3),
]

# Define a style for button
style = ttk.Style()
style.configure("Custom.TButton", font=("comic-sans",16), foreground="black", background="#884EA0", borderwidth = 0)

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == 'C':
        command = clear_entry
    elif text == '=':
        command = calculate_result
    elif text == 'pi':
        command = append_pi
    elif text == '(' or text == ')':
        command = lambda value=text: append_to_entry(value)
    elif text == '%':
        command = lambda: append_to_entry('%')
    else:
        command = lambda value=text: append_to_entry(value)

    ttk.Button(button_frame, text=text, command=command, style = "Custom.TButton",width=8).grid(row=row, column=col, padx= 1, pady= 1, ipady = 30)

# Copyright label
copyright_label = ttk.Label(window, text="© 2025 manman", font=("Arial", 16), foreground="darkgray", background="#4A235A")
copyright_label.pack(side="bottom", pady=25) 

window.mainloop()
