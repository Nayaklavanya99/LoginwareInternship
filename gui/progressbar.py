from tkinter import *
from tkinter.ttk import Progressbar
from time import *
window = Tk()
window.geometry("1920x1080")
window.title("Registration Form")
window.configure(bg="white")


progress = Progressbar(window, orient=HORIZONTAL, length=300, mode='determinate',value=40)
progress3 = Progressbar(window, orient=VERTICAL, length=300, mode='determinate',value=40)
progress4 = Progressbar(window, orient=VERTICAL, length=300, mode='determinate',value=40)
progress2 = Progressbar(window, orient=HORIZONTAL, length=300, mode='indeterminate',value=40)
progress.pack(pady=20)
progress2.pack(pady=20)
progress3.pack(padx=20)
progress4.pack(padx=20)

def mover():
    # for i in range(0,101,10):
    #     progress["value"]=i
    #     progress2["value"]=i
    #     progress3["value"]=i
    #     progress4["value"]=i
    #     window.update_idletasks()
    #     sleep(0.1) 
    # for j in range(100, -1, -10):
    #     progress["value"]=j
    #     progress2["value"]=j
    #     progress3["value"]=j
    #     progress4["value"]=j
    #     window.update_idletasks()
    #     sleep(0.1)
    progress.start(1)
    progress2.start(1)
    progress3.start(1)
    progress4.start(1)

    
def stopper():
    progress.stop()
    progress2.stop()    
    progress3.stop()    
    progress4.stop()
def getValue():
    # progress.cget("value")
    print(progress.cget("value"))
    
getValue()
btn = Button(window, text="Move", width=30, command=mover)
btn2 = Button(window, text="Stop", width=30, command=stopper)
btn.place(x=900,y=600)
btn2.place(x=0,y=600)
window.mainloop()
