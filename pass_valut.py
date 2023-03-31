import sqlite3, hashlib
from tkinter import * 

window =Tk()

window.title("Password Vault")

def login_screen():
    window.geometry("350x150")

    lb=Label(window, text="Enter Master Key")
    lb.config(anchor=CENTER)
    lb.pack(pady=10)

    txt=Entry(window, width=15,show="*") #ENtry dialog for passkey with hidden
    txt.pack()
    txt.focus()

    lbp=Label(window)
    lbp.pack()

    def checkpass():
        passkey='text'

        if passkey==txt.get():
            lbp.config(text="Welcome!")

        else:
            lbp.config(text="Wrong PassKey")

    btn=Button(window, text="Verify",command=checkpass)
    btn.pack(pady=10)

def passvault():
    for widget in window.winfo_children(): #destroys the rest of the widgets
        widget.destroy()

login_screen()

window.mainloop()
