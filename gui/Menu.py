from tkinter import *
from tkinter.ttk import Menubutton


window = Tk()
window.geometry("1920x1080")
window.title("Registration Form")
window.configure(bg="white")

fileOperations=["New","Open","","Save","save as","","Close"]
editOperations=["Cut","Copy","","Undo","Redo","","Rename"]
viewOperations= ["Zoom In","Zoom Out","","Full Screen","","Restore"]
menubar = Menu(window)
file = Menu(menubar, tearoff=0)
edit = Menu(menubar, tearoff=0)
view = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
menubar.add_cascade(label="Edit", menu=edit)
menubar.add_cascade(label="View", menu=view)
for i in fileOperations:
    file.add_command(label=i)
    if i == "":
        file.add_separator()
    if i == "Close":
        file.add_command(command=window.destroy)
    # file.add_separator()
for i in editOperations:
    edit.add_command(label=i)
    if i == "":
      edit.add_separator()
for i in viewOperations:
    view.add_command(label=i)
    if i == "":
        view.add_separator()
Menu.configure(window,menu=menubar)
window.mainloop()
