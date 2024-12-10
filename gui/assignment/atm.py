from tkinter import *

window = Tk()
window.geometry("1920x1080")
window.title("ATM FOR BROKE")
window.configure(bg="#E6F3FF")  # Light blue background

balance = 1000
pin = "broke"


window.update()  
center_x = window.winfo_width() // 2
center_y = window.winfo_height() // 2
Label(window, text="WELCOME TO BROKE ATM", bg="#E6F3FF", fg="red", font=("Jokerman", 24)).place(
    x=center_x- 200 , y=center_y - 150
)  # Dark blue text

Label(window, text="Enter PIN Brokie:", bg="#E6F3FF", fg="magenta", font=("Arial", 12)).place(
    x=center_x - 70, y=center_y - 100
)  # Dark blue text
pin_entry = Entry(window, show="*", bg="#F0F8FF",fg="red",width=25) 
pin_entry.place(x=center_x - 75, y=center_y - 70)


def check_balance():
    balance_window = Toplevel(window)
    balance_window.geometry("200x100")
    balance_window.title("Balance")
    balance_window.configure(bg="#E6F3FF")  # Light blue background
    Label(
        balance_window,
        text=f"Your balance is:\n${balance}",
        bg="#E6F3FF",
        fg="#000080",  # Dark blue text
        font=("Arial", 12),
    ).place(x=100, y=50, anchor=CENTER)


def withdraw():
    def perform_withdrawal():
        global balance
        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                result_label.config(
                    text="Enter positive amount", fg="#8B0000"
                )  # Dark red text
            elif amount > balance:
                result_label.config(
                    text="Insufficient funds", fg="#8B0000"
                )  # Dark red text
            else:
                balance -= amount
                result_label.config(
                    text=f"Withdrawn: ${amount}\nNew balance: ${balance}", fg="#000080"
                )  # Dark blue text
                amount_entry.delete(0, END)
        except ValueError:
            result_label.config(
                text="Enter valid amount", fg="#8B0000"
            )  # Dark red text

    withdraw_window = Toplevel(window)
    withdraw_window.geometry("400x300")
    withdraw_window.title("Withdraw")
    withdraw_window.configure(bg="#E6F3FF")  # Light blue background

    Label(withdraw_window, text="Enter amount:", bg="#E6F3FF", fg="#000080").place(
        x=200, y=100, anchor=CENTER
    )
    amount_entry = Entry(withdraw_window, bg="#F0F8FF")  # Alice blue background
    amount_entry.place(x=200, y=130, anchor=CENTER)

    Button(
        withdraw_window,
        text="Withdraw",
        command=perform_withdrawal,
        bg="#4169E1",
        fg="white",
    ).place(
        x=200, y=160, anchor=CENTER
    )  # Royal blue button
    result_label = Label(withdraw_window, text="", bg="#E6F3FF")
    result_label.place(x=200, y=190, anchor=CENTER)


def deposit():
    def perform_deposit():
        global balance
        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                result_label.config(
                    text="Enter positive amount", fg="#8B0000"
                )  # Dark red text
            else:
                balance += amount
                result_label.config(
                    text=f"Deposited: ${amount}\nNew balance: ${balance}", fg="#000080"
                )  # Dark blue text
                amount_entry.delete(0, END)
        except ValueError:
            result_label.config(
                text="Enter valid amount", fg="#8B0000"
            )  # Dark red text

    deposit_window = Toplevel(window)
    deposit_window.geometry("400x300")
    deposit_window.title("Deposit")
    deposit_window.configure(bg="#E6F3FF")  

    Label(deposit_window, text="Enter amount:", bg="#E6F3FF", fg="#000080").place(
        x=200, y=100, anchor=CENTER
    )
    amount_entry = Entry(deposit_window, bg="#F0F8FF")  
    amount_entry.place(x=200, y=130, anchor=CENTER)

    Button(
        deposit_window,
        text="Deposit",
        command=perform_deposit,
        bg="#4169E1",
        fg="white",
    ).place(
        x=200, y=160, anchor=CENTER
    )  # Royal blue button
    result_label = Label(deposit_window, text="", bg="#E6F3FF")
    result_label.place(x=200, y=190, anchor=CENTER)


def verify_pin():
    if pin_entry.get() == pin:
        atm_window = Toplevel(window)
        atm_window.geometry("400x300")
        atm_window.title("ATM Menu")
        atm_window.configure(bg="#E6F3FF")  # Light blue background

        Label(
            atm_window,
            text="Select Operation",
            bg="#E6F3FF",
            fg="#000080",
            font=("Arial", 12),
        ).place(x=200, y=50, anchor=CENTER)

        Button(
            atm_window,
            text="Check Balance",
            command=check_balance,
            width=15,
            bg="#4169E1",
            fg="white",
        ).place(
            x=200, y=100, anchor=CENTER
        )  # Royal blue buttons
        Button(
            atm_window,
            text="Withdraw",
            command=withdraw,
            width=15,
            bg="#4169E1",
            fg="white",
        ).place(x=200, y=150, anchor=CENTER)
        Button(
            atm_window,
            text="Deposit",
            command=deposit,
            width=15,
            bg="#4169E1",
            fg="white",
        ).place(x=200, y=200, anchor=CENTER)
    else:
        error_label.config(text="Wrong PIN!", fg="#FF0000")  # Bright red for errors
        pin_entry.delete(0, END)


Button(
    window, text="Access", command=verify_pin, width=20, bg="Black", fg="white"
).place(
    x=center_x - 75, y=center_y - 40
)  # Royal blue button
error_label = Label(
    window, text="", bg="#E6F3FF", fg="#FF0000"
)  # Light blue background, red text for errors
error_label.place(x=center_x - 75, y=center_y)

window.mainloop()
