from tkinter import *

window = Tk()
window.geometry("400x600")
window.title("Colorful ATM")
window.configure(bg="#87CEEB")  # Sky blue background

# Initialize balance
balance = 1000
pin = "1234"

# Main login screen with title
title_label = Label(window, 
                   text="Welcome to ATM", 
                   bg="#87CEEB", 
                   fg="#000080",  # Navy blue text
                   font=("Arial", 20, "bold"))
title_label.place(x=110, y=30)

Label(window, 
      text="Enter PIN:", 
      bg="#87CEEB", 
      fg="#000080",
      font=("Arial", 14)).place(x=150, y=100)

pin_entry = Entry(window, show="*", width=20)
pin_entry.place(x=120, y=140)

def check_balance():
    balance_window = Toplevel(window)
    balance_window.geometry("300x200")
    balance_window.title("Balance")
    balance_window.configure(bg="#E0FFFF")  # Light cyan
    
    Label(balance_window, 
          text=f"Your balance is:\n${balance}", 
          bg="#E0FFFF",
          fg="#000080",
          font=("Arial", 14, "bold")).place(x=70, y=60)

def withdraw():
    def perform_withdrawal():
        global balance
        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                result_label.config(text="Enter positive amount")
            elif amount > balance:
                result_label.config(text="Insufficient funds")
            else:
                balance -= amount
                result_label.config(text=f"Withdrawn: ${amount}\nNew balance: ${balance}")
                amount_entry.delete(0, END)
        except ValueError:
            result_label.config(text="Enter valid amount")

    withdraw_window = Toplevel(window)
    withdraw_window.geometry("300x250")
    withdraw_window.title("Withdraw")
    withdraw_window.configure(bg="#E0FFFF")
    
    Label(withdraw_window, 
          text="Enter amount:", 
          bg="#E0FFFF",
          fg="#000080",
          font=("Arial", 12)).place(x=40, y=40)
    
    amount_entry = Entry(withdraw_window)
    amount_entry.place(x=40, y=80)
    
    Button(withdraw_window, 
           text="Withdraw",
           bg="#4169E1",  # Royal Blue
           fg="white", 
           command=perform_withdrawal).place(x=40, y=120)
    
    result_label = Label(withdraw_window, 
                        text="",
                        bg="#E0FFFF",
                        fg="#000080")
    result_label.place(x=40, y=160)

def deposit():
    def perform_deposit():
        global balance
        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                result_label.config(text="Enter positive amount")
            else:
                balance += amount
                result_label.config(text=f"Deposited: ${amount}\nNew balance: ${balance}")
                amount_entry.delete(0, END)
        except ValueError:
            result_label.config(text="Enter valid amount")

    deposit_window = Toplevel(window)
    deposit_window.geometry("300x250")
    deposit_window.title("Deposit")
    deposit_window.configure(bg="#E0FFFF")
    
    Label(deposit_window, 
          text="Enter amount:", 
          bg="#E0FFFF",
          fg="#000080",
          font=("Arial", 12)).place(x=40, y=40)
    
    amount_entry = Entry(deposit_window)
    amount_entry.place(x=40, y=80)
    
    Button(deposit_window, 
           text="Deposit",
           bg="#4169E1",
           fg="white", 
           command=perform_deposit).place(x=40, y=120)
    
    result_label = Label(deposit_window, 
                        text="",
                        bg="#E0FFFF",
                        fg="#000080")
    result_label.place(x=40, y=160)

def verify_pin():
    if pin_entry.get() == pin:
        # Show ATM menu
        atm_window = Toplevel(window)
        atm_window.geometry("300x400")
        atm_window.title("ATM Menu")
        atm_window.configure(bg="#E0FFFF")
        
        Label(atm_window, 
              text="Select Operation", 
              bg="#E0FFFF",
              fg="#000080",
              font=("Arial", 16, "bold")).place(x=70, y=40)
        
        Button(atm_window, 
               text="Check Balance",
               bg="#4169E1",
               fg="white",
               width=15,
               command=check_balance).place(x=80, y=100)
        
        Button(atm_window, 
               text="Withdraw",
               bg="#4169E1",
               fg="white",
               width=15,
               command=withdraw).place(x=80, y=150)
        
        Button(atm_window, 
               text="Deposit",
               bg="#4169E1",
               fg="white",
               width=15,
               command=deposit).place(x=80, y=200)
    else:
        error_label.config(text="Wrong PIN!")
        pin_entry.delete(0, END)

# Login button
Button(window, 
       text="Login",
       bg="#4169E1",
       fg="white",
       width=20,
       command=verify_pin).place(x=120, y=180)

error_label = Label(window, 
                   text="",
                   bg="#87CEEB",
                   fg="red",
                   font=("Arial", 12))
error_label.place(x=120, y=220)

window.mainloop()
