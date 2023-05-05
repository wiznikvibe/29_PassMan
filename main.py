from tkinter import *
from tkinter import messagebox
import string
import random
import json

"""
    ##-------------- Catching Exceptions and throwing errors --------------##
    try:
        Something that might cause an exception
    except Exception as e:
        Do this  if there was an exception
    else:
        Carry this out if there were no exceptions
    finally:
        Carry this out no matter what happens 
"""



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    aplhabets = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    

    pwd_let = [random.choice(aplhabets) for _ in range(random.randint(8,10))]
    pwd_num = [random.choice(numbers) for _ in range(random.randint(2,4))]
    pwd_sym = [random.choice(symbols) for _ in range(random.randint(2,4))]

    pwdList = pwd_let + pwd_num + pwd_sym
    random.shuffle(pwdList)
    password = "".join(pwdList)
    password_entry.insert(0,password)
   




# ---------------------------- SAVE PASSWORD ------------------------------- #
def pass_save():
    website = web_entry.get()
    user_mail = user_entry.get()
    password = pwd_entry.get()

    new_data = {
        website: {
            'email': user_mail,
            'password': password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title='OOps', message="Please make sure to not leave any fields empty.")
    
    else:
        try:
            # If the file already exists then read the file
            with open('data.json','r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # If file not found create the file and dump the new data into it
            with open('data.json','w') as data_file:
                json.dump(new_data,data_file, indent=4)
        else:
            # if Try block executes then update the existing data 
            data.update(new_data)

            with open('data.json','w') as data_file:
            
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END) 

# ---------------------------- Search Credentials --------------------- #

def search_cred():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")       

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passcode Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@xyz.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=search_cred)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=gen_pass)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=pass_save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()