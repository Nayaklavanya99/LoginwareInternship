from tkinter import *
from  tkinter import  Tk
from tkinter import messagebox
from time import sleep
window = Tk()
window.geometry("1920x1080")
window.configure(bg="white")
window.title("Message Box")

def clicked():
    value = messagebox.askquestion("Box","Do you want to exit?")
    if value == "yes":
        box = messagebox.showwarning("Warning","Destroying window")
        print(box)
        messagebox.showerror("Error", "Error in destroying")
        sleep(1)
        value2= messagebox.askokcancel("Box", "Do you want to exit?")
        if value2 == True:
            messagebox.showinfo("Info", "Exiting")
            window.destroy()
    
    
btn = Button(window, text="Click Me", command=clicked)
btn.place(x=900,y=600)
window.mainloop()
