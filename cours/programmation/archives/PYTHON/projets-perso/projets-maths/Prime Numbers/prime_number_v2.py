import tkinter as tk
from tkinter import Canvas, Scrollbar, Frame, messagebox
import math

def sieve_of_eratosthenes(max):
    sieve = [True] * (max + 1)
    sieve[0] = sieve[1] = False

    p = 2
    while (p * p <= max):
        if (sieve[p] == True):
            for i in range(p * p, max + 1, p):
                sieve[i] = False
        p += 1

    return sieve

def update_sieve():
    try:
        max_value = int(entry.get())
        if max_value < 2:
            prime_count_label.config(text="There is 0 prime numbers")
            messagebox.showerror("Invalid Input", "Please enter a number greater than 1.")
            return

        sieve = sieve_of_eratosthenes(max_value)
        draw_sieve(max_value, sieve)

        prime_count = sum(sieve)
        prime_count_label.config(text=f"There is {prime_count} prime numbers")

    except ValueError:
        prime_count_label.config(text="There is 0 prime numbers")
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def draw_sieve(max_value, sieve):
    canvas.delete("all")
    cell_size = 40
    margin = 20
    text_size = 16
    cols = math.ceil(math.sqrt(max_value)) + 1

    canvas_width = cols * cell_size + 2 * margin
    canvas_height = ((max_value // cols) + 1) * cell_size + 2 * margin

    x_offset = (canvas.winfo_width() - canvas_width) // 2 if canvas.winfo_width() > canvas_width else margin

    for num in range(max_value + 1):
        row = num // cols
        col = num % cols
        x0 = col * cell_size + x_offset
        y0 = row * cell_size + margin
        x1 = x0 + cell_size
        y1 = y0 + cell_size
        if sieve[num]:
            canvas.create_rectangle(x0, y0, x1, y1, fill='red')
            canvas.create_text(x0 + cell_size / 2, y0 + cell_size / 2, text=str(num), fill='white', font=("Helvetica", text_size, "bold"))
        else:
            canvas.create_rectangle(x0, y0, x1, y1, fill='white')
            canvas.create_text(x0 + cell_size / 2, y0 + cell_size / 2, text=str(num), fill='black', font=("Helvetica", text_size))

    canvas.configure(scrollregion=(0, 0, canvas_width, canvas_height))

root = tk.Tk()
root.title("Sieve of Eratosthenes")

title_label = tk.Label(root, text="Generating of prime numbers until a maxima", font=("Helvetica", 18))
title_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

entry_label = tk.Label(input_frame, text="Please enter a maxima: ")
entry_label.pack(side=tk.LEFT)

entry = tk.Entry(input_frame)
entry.pack(side=tk.LEFT)

update_button = tk.Button(input_frame, text="Update list", command=update_sieve)
update_button.pack(side=tk.LEFT, padx=10)

scroll_frame = Frame(root)
scroll_frame.pack(pady=10, fill=tk.BOTH, expand=True)

canvas = Canvas(scroll_frame, width=800, height=600)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(scroll_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

prime_count_label = tk.Label(root, text="There is 0 prime numbers", font=("Helvetica", 24))
prime_count_label.pack(pady=10)

root.mainloop()
