from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Radiobutton, messagebox
import sqlite3 as sl
from tkinter import Toplevel
from time import sleep

conn = sl.connect("College.db")

cur = conn.cursor()

# cur.execute("DROP TABLE IF EXISTS Registration")

window = Tk()
window.geometry("1920x1080")
window.title("Registration Form")
window.configure(bg="white")

list1 = ["Name", "DoB", "Number", "EmailId", "College", "Course", "Usn", "Gender"]
genders = ["Male", "female", "Others"]

lbl = Label(
    window,
    text="Registration Form",
    bg="white",
    fg="Black",
    font=("Roboto", 20),
    width=20,
)
lbl.place(x=550, y=20)
# Create table query
create_table_query = """CREATE TABLE IF NOT EXISTS Registration(
    Name TEXT NOT NULL DEFAULT 'Not Provided',
    DoB TEXT NOT NULL DEFAULT 'Not Provided', 
    Number TEXT NOT NULL DEFAULT 'Not Provided',
    EmailId TEXT NOT NULL UNIQUE DEFAULT 'Not Provided',
    College TEXT NOT NULL DEFAULT 'Not Provided',
    Course TEXT NOT NULL DEFAULT 'Not Provided',
    Usn TEXT NOT NULL UNIQUE DEFAULT 'Not Provided',
    Gender TEXT NOT NULL DEFAULT 'Not Provided'
)"""
cur.execute(create_table_query)

entries = []  

valx = 500
valy = 100
for field in list1:
    lbl2 = Label(window, text=field, bg="white", fg="Black", font=("Roboto", 9))
    lbl2.place(x=valx, y=valy)
    valy += 50

valx = 700
valy = 450
gen = StringVar()
for i in genders:
    check = Radiobutton(
        window, text=i, bg="white", font=("Roboto", 9), variable=gen, value=i
    )
    check.place(x=valx, y=valy)
    valy += 30

valx = 700
valy = 100
for i in range(len(list1) - 2):
    if i == 5:
        combo = Combobox(window, width=37)
        combo["values"] = ("B.Tech", "M.Tech", "B.Sc", "M.Sc","MCA")
        combo.place(x=valx, y=valy)
        entries.append(combo)
        valy += 50
    entry = Entry(window, width=40, bg="lightgrey")
    entry.place(x=valx, y=valy)
    entries.append(entry)
    valy += 50
entries.append(gen)
list1.append("Gender")
# print(list1)


def validate_form():

    if not entries[0].get().replace(" ", "").isalpha():
        messagebox.showerror("Error", "Name should contain only letters")
        return False
    
    if not entries[2].get().isdigit() or len(entries[2].get()) != 10:
        messagebox.showerror("Error", "Phone number should be 10 digits")
        return False

    email = entries[3].get()
    if "@" not in email or "." not in email.split("@")[-1]:
        messagebox.showerror("Error", "Invalid email format")
        return False
    
    for i in range(len(entries)):
        if not entries[i].get():
            if entries[i].get() == "DoB":
                messagebox.showerror("Error", "Gender cannot be empty")
            messagebox.showerror("Error", f"{list1[i]} cannot be empty")
            return False

    return True

def send():
    if not validate_form():
        return
    print("Sending")
    list2 = []  
    for i in range(len(list1) - 1):
        print(list1[i] + " : " + entries[i].get())
        list2.append(entries[i].get())
    for entry in entries[:-1]:
        entry.delete(0, END)
    gen.set(NONE)
    
    try:
        insert_query = (
            """INSERT INTO Registration (Name,DoB,Number,EmailId,College,Course,Usn,Gender) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        )
        ch = messagebox.askyesno("Confirmation", "Are you sure you want to submit?")
        if not ch:
            return
        cur.execute(insert_query, list2)  
        conn.commit()
        messagebox.showinfo("Success", "Registration completed successfully!")
        window.destroy()
        window2 = Toplevel()
        window2.geometry("1920x1080")
        window2.title("Registration Form")
        window2.configure(bg="white")
        lbl = Label(
            window2,
            text="Registration Complete!!",
            bg="white", 
            fg="Black",
            font=("Roboto", 20),
            width=20,
        )
        lbl.place(x=450, y=250)
        window2.after(2000, window2.destroy)
        window2.mainloop()   
    except sl.IntegrityError:
        messagebox.showerror("Error", "Email or Usn Already exists!")
    except:
        messagebox.showerror("Error", "Something went wrong!")


btn = Button(window, text="Register", command=send, width=30)
btn.place(x=530, y=valy + 90)

window.mainloop()
