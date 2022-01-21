from distutils import command
from doctest import master
from tabnanny import check
import tkinter as tk
import receipt
import functools
import data


selected_colleges = []
college_checkboxes = {}

def create_college_checkboxes() :
    college_list = data.get_colleges()
    for college in college_list :
        college_checkboxes.update({college:0})

def process():
    for status in college_checkboxes : 
        print(college_checkboxes[status])

    print(selected_colleges)
    

def updateCheck(college) :
    print(college)
    check_status = college_checkboxes.get(college)
    if check_status == 0 :
        college_checkboxes[college] = 1
        add_college(college)
    elif check_status == 1 :
        college_checkboxes[college] = 0
        remove_college(college)


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

    button = tk.Button(text="Start", command=lambda:process())
    button.grid(row=4, column=1, padx=10, pady=10)

    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)


def create_checkboxes(root) :
    checkboxes_frame = tk.Frame(master=root)

    create_college_checkboxes()

    colleges = data.get_colleges()

    for college_name in colleges :
        tk.Checkbutton(
            master = checkboxes_frame, 
            text=college_name, 
            command=functools.partial(updateCheck(college_name)) 
        ).pack()
        print(college_name)
    
    checkboxes_frame.grid(row=3, column=0, columnspan=2,sticky='NESW')

    

    

    

def buildApp() :
    window = tk.Tk()
    createBotFrame(window)
    window.mainloop()

buildApp()