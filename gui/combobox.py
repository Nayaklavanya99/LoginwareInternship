from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.geometry("1920x1080")
window.title("Radio")
window.configure(bg="white")


# listofChoice = ["Kannada", "English", "Hindi"]
listofoption=["Date","Month","Year"]
listofDate =["12","22","11"]
listofMonth =["09","07","08"]
listofyear =["2002","2001","1997"]
listoflist=[listofDate,listofMonth,listofyear]

valx = 200
valy = 200
k=0
varss = [date, Month, year]
for i in listoflist:
    varss[k] = Combobox(window, width=30,values=i[0:],background="Black",foreground="Red")
    varss[k].set(listofoption[k])
    k+=1
    varss[k].place(x=valx,y=valy)
    valx += 220

def assign():
    for i in range(len(varss)):
        print(varss[i].get())
def submit():
    print(f"Submitted choice: {box.get()}") 

btn = Button(window, text="Submit", width=30, command=submit)
btn.place(x=200,y=250)


window.mainloop()
