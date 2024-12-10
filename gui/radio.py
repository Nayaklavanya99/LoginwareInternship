from tkinter import *
from tkinter import Radiobutton

window = Tk()
window.geometry("1920x1080")
window.title("Radio")
window.configure(bg="white")


selected_language = StringVar()

listofChoice = ["Kannada","English","Hindi"]
valx = 500
valy = 200

llb1 = Label(window, text="Select your language", font=("ROBOTO", 14))
def on_select():
    selected = selected_language.get()
    print(f"Selected language: {selected}") 

for i in listofChoice:
    radio = Radiobutton(
        window, 
        text=i, 
        value=i, 
        bg="white",
        variable=selected_language,  
        command=on_select,
        font=("ROBOTO", 14),  
    )
    radio.place(x=valx,y=valy)
    valy += 30

lbl =None
def submit_choice():
    selected = selected_language.get()
    global lbl
    if lbl:
        lbl.destroy()
        lbl = None
    lbl = Label(window, text=f"Submitted choice: {selected}", font=("ROBOTO", 14))
    lbl.place(x=500, y=350)


btn = Button(window, text="Submit", width=30, command=submit_choice)
btn.place(x=500, y=290)

window.mainloop()
