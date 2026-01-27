import tkinter as tk
from tkinter import messagebox

calculator = tk.Tk()
calculator.title("Calculator")
calculator.geometry("500x500")
calculator.configure(bg='white')

def equal():
    try:
        expression = screen.get()
        result = str(eval(expression))
        screen.delete(0, tk.END)
        screen.insert(0, result)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")
        screen.delete(0, tk.END)

def click(num):
    screen.insert(tk.END, num)

def clear_screen():
    display_text.set("")

display_text = tk.StringVar()
screen = tk.Entry(calculator, textvariable=display_text, font=("Arial", 24), justify='right', bd=10)
screen.grid(row=0, column=0, columnspan=4, padx=50, pady=30)

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1), ('+', 5, 0), ('-', 5, 1),
    ('*', 5, 2), ('/', 6, 0)
]

for txt, r, c in buttons:
    # We use lambda so the function doesn't run immediately
    tk.Button(calculator, text=txt, padx=15, pady=5, width=3,
              command=lambda t=txt: click(t)).grid(row=r, column=c, pady=2)

# Removed the () from clear_screen so it only runs on click
tk.Button(calculator, text="Clear", padx=15, pady=5, width=12,
          command=clear_screen).grid(row=6, column=1, columnspan=2, pady=2)

tk.Button(calculator, text="=", padx=15, pady=5, width=9,
          command=equal).grid(row=7, column=0, columnspan=3, pady=2)

# This MUST be the very last line of your script
calculator.mainloop()