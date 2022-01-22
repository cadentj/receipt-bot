import tkinter as tk
import receipt
import functools
import data


selected_colleges = []
college_checkboxes = {}

def initialize_college_dic() :
    college_list = data.get_colleges()
    for college in college_list :
        college_checkboxes.update({college:0})

def process():
    data.create_email_list(selected_colleges)
    receipt.start()

    

def update_check(college) :
    print(college)
    check_status = college_checkboxes.get(college)
    if check_status == 0 :
        college_checkboxes[college] = 1
        selected_colleges.append(college)
    elif check_status == 1 :
        college_checkboxes[college] = 0
        selected_colleges.remove(college)


# Initializes checkboxes to dictionary
def create_checkboxes(root) :
    checkboxes_frame = tk.Frame(master=root)

    initialize_college_dic()

    colleges = data.get_colleges()

    for college_name in colleges :
        tk.Checkbutton(
            master = checkboxes_frame, 
            text=college_name, 
            command= functools.partial(update_check, college_name)
        ).pack()
        print(college_name)
    
    checkboxes_frame.grid(row=3, column=0, columnspan=2,sticky='NESW')


def create_bot_frame(root) :

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



    

    

def build_app() :
    root = tk.Tk()
    create_bot_frame(root)
    root.mainloop()

build_app()