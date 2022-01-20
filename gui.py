import tkinter as tk
import test

def process():
    lbl_value["text"] = "Processing..."
    user = username.get()
    passw = password.get()
    test.start(user, passw)
    


window = tk.Tk()

username = tk.Entry(fg="yellow", bg="blue", width=50)
username.pack()

password = tk.Entry(fg="yellow", bg="black", width=50)
password.pack()




btn_start = tk.Button(master=window, text="Start", command=process)
btn_start.pack()


lbl_value = tk.Label(master=window, text="0")
lbl_value.pack()

window.mainloop()