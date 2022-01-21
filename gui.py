from doctest import master
from tabnanny import check
import tkinter as tk
import receipt
import data


selected_colleges = []
college_checkboxes = {}
college_list = data.get_colleges()

def create_college_checkboxes() :
    for college in college_list :
        college_checkboxes.update({college, 0})



def process():
    print(selected_colleges)
    

def isChecked(college_name) :
    if college_checkboxes.get(college_name) == 1:
        add_college(college_name)
    if college_checkboxes.get() == 0:
        remove_college(college_name)    


def add_college(college_name) :
    selected_colleges.append(college_name)


def remove_college(college_name) :
    selected_colleges.remove(college_name) 


def createBotFrame(root) :

    # Set constant window size
    root.minsize(300, 400)    
    root.maxsize(300, 400)

    # Create and add title label and entry box
    title = tk.Label(
        text="Receipt Bot",
        font=(20),
    )
    title.grid(row=0, column=0, columnspan=2)

    # Create and add username label and entry box
    user = tk.Label(
        text="Username",
    )
    user_entry = tk.Entry(
    )
    user.grid(row=1,column=0,sticky='NESW')
    user_entry.grid(row=1, column=1,sticky='NESW', padx=10, pady=10)

    # Create and add password label and entry box
    password = tk.Label(
        text="Password",
    )
    password_entry = tk.Entry(
    )
    password.grid(row=2, column=0,sticky='NESW')
    password_entry.grid(row=2, column=1,sticky='NESW', padx=10, pady=10)

    # Create and add checkboxes
    create_checkboxes(root)

    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)


def create_checkboxes(root) :
    checkboxes_frame = tk.Frame(master=root)

    create_college_checkboxes()

    colleges = data.get_colleges()
    for college_name in colleges :
        check = tk.Checkbutton(
            master = checkboxes_frame, 
            text=college_name, 
            variable = college_checkboxes[college_name],
            onvalue=1,
            offvalue=0,
            command=isChecked(college_name)
        )
        check.pack()
        
    
    checkboxes_frame.grid(row=3, column=0, columnspan=2,sticky='NESW')

    

    

    

def buildApp() :
    window = tk.Tk()
    createBotFrame(window)
    window.mainloop()

buildApp()