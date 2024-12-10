from tkinter import *

window = Tk()
window.geometry("1920x1080") 
window.title("Registration Form")
window.configure(bg="white")

# Global label variable
lbl = None

def clicked():
    value = hscale.get()
    global lbl
    if lbl:
        lbl.destroy()
    lbl = Label(window, text=f"Are You sure about that: {value} value", bg="white", fg="Black", font=("Roboto", 9))
    lbl.pack()

def showvalue(value):
    global lbl
    if lbl:
        lbl.destroy()
    lbl = Label(window, text=f"Current value: {value} value", bg="white", fg="Black", font=("Roboto", 9))
    lbl.pack()
    try:
        window.config(bg=f"#ff{str(value)}{value}")
        btn.config(bg=f"#f3{value}")
        btn2.config(bg=f"#f{str(value)}{value}{str(value)}")
    except:
        window.config(bg=f"#f{value}")
        btn.config(bg=f"#e{value}")
        btn2.config(bg="#ffeede")


hscale = Scale(window, from_=0, to=100, orient=VERTICAL, cursor="circle", length=300, width=20, 
               bg="lightblue", fg="red", activebackground="green", troughcolor="yellow", 
               tickinterval=10, command=showvalue)

# Reset function - sets scale to 0 and removes label
def reset():
    hscale.set(0)
    global lbl
    if lbl:
        lbl.destroy()

# Create Submit and Reset buttons
btn = Button(window, text="Submit", width=30, command=clicked)
btn2 = Button(window, text="Reset", width=30, command=reset)

# Pack all widgets into window
hscale.pack()
btn.pack()
btn2.pack()

# Start the Tkinter event loop
window.mainloop()
