from tkinter import *
from math import sin, cos, tan, sqrt, radians


# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + value)


# Function to clear the entry box
def clear():
    entry.delete(0, END)


# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")


# Function to handle scientific operations
def scientific_op(op):
    try:
        value = float(entry.get())
        entry.delete(0, END)
        if op == "sin":
            entry.insert(END, sin(radians(value)))
        elif op == "cos":
            entry.insert(END, cos(radians(value)))
        elif op == "tan":
            entry.insert(END, tan(radians(value)))
        elif op == "sqrt":
            entry.insert(END, sqrt(value))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")


# Main application window
window = Tk()
window.title("Simple Calculator")
window.geometry("300x400")

# Entry box
entry = Entry(window, width=25, font=("Arial", 16), borderwidth=2, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("+", 4, 2),
    ("=", 4, 3),
    ("C", 5, 0),
    ("sin", 5, 1),
    ("cos", 5, 2),
    ("tan", 5, 3),
    ("sqrt", 6, 0),
]

# Add buttons to the window
for text, row, col in buttons:
    if text in "0123456789.+-*/":
        btn = Button(
            window, text=text, width=5, height=2, command=lambda t=text: button_click(t)
        )
    elif text == "=":
        btn = Button(window, text=text, width=5, height=2, command=calculate)
    elif text == "C":
        btn = Button(window, text=text, width=5, height=2, command=clear)
    else:
        btn = Button(
            window, text=text, width=5, height=2, command=lambda t=text: scientific_op(t)
        )
    btn.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()
