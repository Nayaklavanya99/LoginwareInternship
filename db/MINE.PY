from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Radiobutton
from tkinter import Radiobutton
import sqlite3 as sl

conn = sl.connect("College.db")

cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS Student")

window = Tk()
window.geometry("1920x1080")
window.title("Registration Form")
window.configure(bg="white")

list1 = ["Name", "DoB", "Number", "EmailId", "College", "Course", "Usn", "Gender"]
genders = ["Male", "female", "Others"]

# Create table query
create_table_query = """CREATE TABLE IF NOT EXISTS Registration(
    Name TEXT NOT NULL DEFAULT 'Not Provided',
    DoB TEXT NOT NULL DEFAULT 'Not Provided', 
    Number TEXT NOT NULL DEFAULT 'Not Provided',
    EmailId TEXT NOT NULL UNIQUE DEFAULT 'Not Provided',
    College TEXT NOT NULL DEFAULT 'Not Provided',
    Course TEXT NOT NULL DEFAULT 'Not Provided',
    Usn TEXT NOT NULL DEFAULT 'Not Provided',
    Gender TEXT NOT NULL DEFAULT 'Not Provided'
)"""
cur.execute(create_table_query)

entries = []

valx = 500
valy = 50
for field in list1:
    lbl2 = Label(window, text=field, bg="white", fg="Black", font=("Roboto", 9))
    lbl2.place(x=valx, y=valy)
    valy += 50

valx = 700
valy = 400
gen = StringVar()
for i in genders:
    check = Radiobutton(
        window, text=i, bg="white", font=("Roboto", 9), variable=gen, value=i
    )
    check.place(x=valx, y=valy)
    valy += 30


valx = 700
valy = 50
for i in range(len(list1) - 2):
    if i == 5:
        combo = Combobox(window, width=40)
        combo["values"] = ("B.Tech", "M.Tech", "B.Sc", "M.Sc", "MCA")
        combo.place(x=valx, y=valy)
        entries.append(combo)
        valy += 50
    entry = Entry(window, width=40, bg="lightgrey")
    entry.place(x=valx, y=valy)
    entries.append(entry)
    valy += 50
entries.append(gen)
list1.append("Gender")
print(list1)


def send():
    print("Sending")
    list2 = []
    for i in range(len(list1) - 1):
        print(list1[i] + " : " + entries[i].get())
        list2.append(entries[i].get())
    print(list2)
    insert_query = """INSERT INTO Registration (Name,DoB,Number,EmailId,College,Course,Usn,Gender) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
    cur.execute(insert_query, list2)
    conn.commit()


btn = Button(window, text="Send", command=send, width=30)
btn.place(x=530, y=valy + 90)

window.mainloop()
