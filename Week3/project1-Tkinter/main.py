
from tkinter import Tk, Label, Entry, Button,ttk
import pandas
import pprint



def search():
    gig_data = pandas.read_csv("GIG-logistics(in).csv")
    gig_data=gig_data.to_dict()
    print(gig_data)
    name_found=False
    dict_key=""
    department=""
    user_name=user_name_input.get()
    departmemt_name=department_dropdown.get()
    all_users_key=[]
    all_users_print=""
    for key,value in gig_data["Name"].items():
        if value==user_name:
            name_found=True
            dict_key=key

    if name_found and departmemt_name==gig_data["Department"][dict_key]:
        print(dict_key)
        department=gig_data["Department"][dict_key]
        print(department)
        for key,value in gig_data["Department"].items():
            if value==department:
                all_users_key.append(key)
        for i in all_users_key:
            user_and_department=f"{gig_data["Name"][i]},{gig_data["Department"][i]}\n"
            all_users_print+=user_and_department
            print(user_and_department)
        all_users.config(text=all_users_print)
    else:
        all_users.config(text="You dont work here")







window=Tk()
window.title("Password Manager")
window.config(pady=20,padx=20)

gig_label=Label(text="GIG_LOGISTICS USER CONFIRMATIOM")
gig_label.grid(row=0,column=1,columnspan=2)

user_name_label=Label(text="Username:")
user_name_label.grid(row=1,column=0)

department_label=Label(text="department:")
department_label.grid(row=2,column=0)

user_name_input=Entry(width=21)
user_name_input.grid(row=1,column=1,columnspan=2)

department_dropdown = ttk.Combobox(window, values=["Technology", "Finance","Customer Service","Sales","Marketing"])
department_dropdown.grid(row=2, column=1, columnspan=2)
department_dropdown["state"] = "readonly"

search_button=Button(text="search" ,command=search)
search_button.grid(column=1,row=3)

all_users=Label(text="")
all_users.grid(row=4,column=0,columnspan=3)
window.mainloop()