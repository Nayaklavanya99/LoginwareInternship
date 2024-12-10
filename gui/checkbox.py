from tkinter import *
from tkinter import Radiobutton

window = Tk()
window.geometry("1920x1080")
window.title("Radio")
window.configure(bg="white")


selected_language = StringVar()

listofChoice = ["Kannada", "English", "Hindi"]
valx = 500
valy = 200

llb1 = Label(window, text="Select your language", font=("ROBOTO", 14))
llb1.pack()

lang = StringVar()
for i in listofChoice:
    check = Checkbutton(window, text=i, bg="white", font=("ROBOTO", 14),onvalue=i,offvalue=None,variable=lang)
    check.pack()
    valy += 30

option = StringVar()

def submit():
    print(f"Submitted choice: {lang.get()}")

btn = Button(window, text="Submit", width=30, command=submit)
btn.pack()
window.mainloop()