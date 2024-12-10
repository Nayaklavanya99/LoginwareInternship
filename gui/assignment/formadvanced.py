from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Radiobutton
from tkinter import Radiobutton
window = Tk()
window.geometry("1920x1080")
window.title("Registration Form")
window.configure(bg="white")

# Define the fields
list1 = [
    "Name",
    "DoB",
    "Number",
    "EmailId",
    "College",
    "Course",
    "Usn",
    "Gender"
]
genders = ["Male","female","Others"]
entries = []  # To store Entry widgets

valx = 500
valy = 50
file_path = "formdetails.doc"

for field in list1:
    lbl2 = Label(window, text=field, bg="white", fg="Black", font=("Roboto", 9))
    lbl2.place(x=valx, y=valy)
    valy += 50
valx = 700
valy = 400
gen = StringVar()
for i in genders:
    check = Radiobutton(window, text=i, bg="white", font=("Roboto", 9),variable=gen,value=i)
    check.place(x=valx,y=valy)
    valy+=30


valx = 700
valy = 100
for i in range(len(list1)-2):
    entry = Entry(window, width=40, bg="lightgrey")
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
    with open(file_path, "a") as file:
        file.write(f"Gender: {gen.get()}\n")
    print(f"Gender: {gen.get()}")


btn = Button(window, text="Send", command=send, width=30)
btn.place(x=530, y=valy + 90)

window.mainloop()
