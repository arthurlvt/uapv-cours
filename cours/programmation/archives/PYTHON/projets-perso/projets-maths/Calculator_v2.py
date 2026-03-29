import tkinter as tk
from tkinter import messagebox

# Function to update the display when a button is clicked
def button_click(number):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, str(current) + str(number))

# Function to perform the calculation and display the result
def calculate():
    try:
        expression = entry_display.get()
        result = eval(expression)  # Use eval() to evaluate the expression
        
        entry_display.delete(0, tk.END)
        entry_display.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Function to clear the display
def clear():
    entry_display.delete(0, tk.END)

# Creating the main window
root = tk.Tk()
root.title("Calculator")

# Configuration of font
large_font = ('Arial', 16)

# Entry widget for display
entry_display = tk.Entry(root, font=large_font, width=15, borderwidth=5)
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button widgets for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=large_font, padx=20, pady=20,
                       command=lambda text=text: button_click(text))
    button.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text='Clear', font=large_font, padx=20, pady=20, command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Running the main event loop
root.mainloop()
