from tkinter import *


window = Tk()
window.geometry("1920x1080")
window.title("Registration Form")
window.configure(bg="white")

hscale = Scale(window, from_=0, to=100, orient=HORIZONTAL, cursor="circle",length=200, width=40,bg="blue",fg="red",activebackground="green",troughcolor="yellow")
vscale = Scale(window, from_=0, to=100, orient=VERTICAL, length=300, width=20,cursor="circle",tickinterval=10)
lbl = NONE
def clicked():
    value =hscale.get()
    global lbl
    lbl = Label(window, text=f"this is how Dumbe you are {value}", bg="white", fg="Black", font=("Roboto", 9))
    lbl.pack()

def reser():
    hscale.set(0)
    lbl.destroy()


btn = Button(window, text="Submit", width=30,command=clicked)
btn2 = Button(window, text="Reset", width=30, command=reser)

hscale.pack()
vscale.pack()   
btn.pack()
btn2.pack()



window.mainloop()