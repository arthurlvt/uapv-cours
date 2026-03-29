import tkinter as tk
from tkinter import messagebox

def multiply():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        result = a * b

        messagebox.showinfo('Result', f"The result of {a} * {b} is {result}")
    
    except ValueError:
        messagebox.showerror('Invalid Input', 'Please, enter a valid number !')


root = tk.Tk()
root.title("Multiplication Calculator")

large_font = ('Arial', 16)

label_a = tk.Label(root, text="What's the first number?", font=large_font)
label_a.pack(padx=10, pady=10)
entry_a = tk.Entry(root, font=large_font)
entry_a.pack(padx=10, pady=10)

label_b = tk.Label(root, text="What's the second number?", font=large_font)
label_b.pack(padx=10, pady=10)
entry_b = tk.Entry(root, font=large_font)
entry_b.pack(padx=10, pady=10)

button = tk.Button(root, text="Calculate", font=large_font, command=multiply)
button.pack(padx=10, pady=20)


root.mainloop()
    