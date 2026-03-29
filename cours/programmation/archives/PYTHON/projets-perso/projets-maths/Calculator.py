import tkinter as tk
from tkinter import messagebox

# Functions for each operation
def sum(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Function to perform the selected operation
def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        operation = operation_var.get()
        
        if operation == "Addition":
            result = sum(a, b)
        elif operation == "Subtraction":
            result = subtraction(a, b)
        elif operation == "Multiplication":
            result = multiplication(a, b)
        elif operation == "Division":
            result = division(a, b)
        else:
            result = "Please select an operation"
        
        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")

# Creating the main window
root = tk.Tk()
root.title("Simple Calculator")

# Configuration of font
large_font = ('Arial', 16)

# Widgets for input
label_a = tk.Label(root, text="Enter the first number:", font=large_font)
label_a.pack(padx=10, pady=10)

entry_a = tk.Entry(root, font=large_font)
entry_a.pack(padx=10, pady=10)

label_b = tk.Label(root, text="Enter the second number:", font=large_font)
label_b.pack(padx=10, pady=10)

entry_b = tk.Entry(root, font=large_font)
entry_b.pack(padx=10, pady=10)

# Dropdown menu for selecting the operation
operation_var = tk.StringVar(root)
operation_var.set("Select Operation")

operations_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
operations_menu.config(font=large_font)
operations_menu.pack(padx=10, pady=10)

# Calculate button
button = tk.Button(root, text="Calculate", font=large_font, command=calculate)
button.pack(padx=10, pady=20)

# Running the main event loop
root.mainloop()
