from tkinter import *
from tkinter.ttk import Menubutton


window = Tk()
window.geometry("1920x1080")
window.title("Registration Form")
window.configure(bg="white")

def click():
    top = Toplevel()
    top.geometry("300x300")
    top.title("New Window")
    top.configure(bg="black",fg="white")
    list1 = [
    "Name",
    "DoB",
    "Number",
    "EmailId",
    "College",
    "Course",
    "Usn",
    "Gender",
    "Skills",
    "Interests",
]
entries = []  # To store Entry widgets

valx = 500
valy = 100
file_path = "formdetails.doc"


for field in list1:
    lbl2 = Label(window, text=field, bg="white", fg="Black", font=("Roboto", 9))
    lbl2.place(x=valx, y=valy)
    valy += 50


    valx = 600
    valy = 100
    for i in range(len(list1)):
        entry = Entry(window, width=40,bg="lightgrey")
        entry.place(x=valx, y=valy)
        entries.append(entry)  
        valy += 50


    def fileformat():
        with open(file_path, "a") as file:
            file.write("-" * 82 + "\n")


    def send():
        fileformat()
        for field, entry in zip(list1, entries):
            value = entry.get()
            print(f"{field}: {value}")

            with open(file_path, "a") as file:
                file.write(f"{field}: {value}\n")
            entry.delete(0, END)


    btn = Button(window, text="Send", command=send, width=30)
    btn.place(x=530, y=valy + 30)
    
    top.mainloop()
    

btn = Button(window, text="Submit", width=30,command=click)
btn.pack()



window.mainloop()