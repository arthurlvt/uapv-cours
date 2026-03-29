import tkinter as tk
from tkinter import messagebox

def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("The number must be odd")
    
    magic_square = [[0] * n for _ in range(n)]
    
    num = 1
    i, j = 0, n // 2
    
    while num <= n * n:
        magic_square[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n
        
        if magic_square[new_i][new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
    
    return magic_square

def show_magic_square():
    try:
        input_text = entry.get().strip()
        
        if input_text == "":
            raise ValueError("What The Fuck You Wanna Do ?")
        
        n = int(input_text)
        
        if n == 0:
            raise ValueError("The number mustn't be zero")
        
        if n % 2 == 0:
            raise ValueError("The number must be odd")
        
        magic_square = generate_magic_square(n)
        display_magic_square(magic_square, n)
        
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def display_magic_square(square, n):
    max_num = n * n
    max_num_len = len(str(max_num))
    
    for widget in magic_frame.winfo_children():
        widget.destroy()
    
    canvas = tk.Canvas(magic_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    v_scrollbar = tk.Scrollbar(magic_frame, orient=tk.VERTICAL, command=canvas.yview)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    canvas.configure(yscrollcommand=v_scrollbar.set)
    
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)
    
    labels = []
    for i in range(n):
        row_labels = []
        for j in range(n):
            cell_value = square[i][j]
            cell_label = tk.Label(frame, text=f'{cell_value}', width=4, height=2, font=("Courier", 24), borderwidth=1, relief="solid")
            cell_label.grid(row=i, column=j)
            cell_label.bind("<Button-1>", lambda event, x=i, y=j: highlight_columns(square, labels, x, y, n))
            row_labels.append(cell_label)
        labels.append(row_labels)
    
    magic_message.config(text=f"The magic number is {n * (n*n + 1) // 2}")
    
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.bind("<Configure>", lambda event, canvas=canvas: on_canvas_configure(canvas))
    
    frame.update_idletasks()
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    frame_width = frame.winfo_reqwidth()
    frame_height = frame.winfo_reqheight()
    
    if canvas_width > frame_width:
        canvas.create_window((canvas_width - frame_width) // 2, 0, window=frame, anchor=tk.NW)
    if canvas_height > frame_height:
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    canvas.bind_all("<MouseWheel>", lambda event, canvas=canvas: on_mouse_wheel(event, canvas))

def highlight_columns(square, labels, row, col, n):
    target_sum = n * (n*n + 1) // 2
    current_sum = 0
    
    if labels:
        for i in range(n):
            for j in range(n):
                labels[i][j].config(bg="white")
    
        if row == col:
            current_sum = sum(square[i][i] for i in range(n))
            if current_sum == target_sum:
                for i in range(n):
                    labels[i][i].config(bg="red")
    
        if row + col == n - 1:
            current_sum = sum(square[i][n - 1 - i] for i in range(n))
            if current_sum == target_sum:
                for i in range(n):
                    labels[i][n - 1 - i].config(bg="red")
    
        current_sum = sum(square[i][col] for i in range(n))
        if current_sum == target_sum:
            for i in range(n):
                labels[i][col].config(bg="red")
    
        current_sum = sum(square[row][j] for j in range(n))
        if current_sum == target_sum:
            for j in range(n):
                labels[row][j].config(bg="red")
    
    else:
        for i in range(n):
            for j in range(n):
                cell_value = square[i][j]
                cell_label = tk.Label(magic_frame, text=f'{cell_value}', width=4, height=2, font=("Courier", 24), borderwidth=1, relief="solid")
                cell_label.grid(row=i, column=j)
                cell_label.bind("<Button-1>", lambda event, x=i, y=j: highlight_columns(square, [], x, y, n))
        
        magic_message.config(text=f"The magic number is {n * (n*n + 1) // 2}")

def on_canvas_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_mouse_wheel(event, canvas):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

root = tk.Tk()
root.title("Magic Square by arthurlvt")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Please enter a size for the magic square (it must be odd) :", font=("Helvetica", 20)).pack(pady=10)

entry = tk.Entry(frame, font=("Helvetica", 16))
entry.pack(pady=5)

tk.Button(frame, text="Generate", command=show_magic_square, font=("Helvetica", 16)).pack(pady=10)

magic_frame = tk.Frame(root)
magic_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

magic_message = tk.Label(root, text="", font=("Helvetica", 24))
magic_message.pack()

root.mainloop()