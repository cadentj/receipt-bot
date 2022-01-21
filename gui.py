import tkinter as tk
from turtle import width
import test


def process():
    lbl_value["text"] = "Processing..."
    user = username.get()
    passw = password.get()
    test.start(user, passw)
    lbl_value["text"] = "Finished"
    



def createBotFrame(root) :

    root.minsize(300, 400)    
    root.maxsize(300, 400)

    title = tk.Label(
        text="Receipt Bot",
        font=(20),
    )
    title.grid(row=0, column=0, columnspan=2)

    user = tk.Label(
        text="Username",
    )
    user_entry = tk.Entry(
    )
    user.grid(row=1,column=0,sticky='NESW')
    user_entry.grid(row=1, column=1,sticky='NESW', padx=10, pady=10)

   
    password = tk.Label(
        text="Password",
    )
    password_entry = tk.Entry(
    )
    password.grid(row=2, column=0,sticky='NESW')
    password_entry.grid(row=2, column=1,sticky='NESW', padx=10, pady=10)

    email = tk.Label(
        text="Emails",
    )
    email_entry = tk.Text(
    )
    email.grid(row=3, column=0,sticky='NESW')
    email_entry.grid(row=4, column=0, columnspan=2,sticky='NESW')

    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    


    

    

def buildApp() :
    window = tk.Tk()
    createBotFrame(window)
    window.mainloop()

buildApp()