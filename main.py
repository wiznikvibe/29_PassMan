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
    pwd_entry.insert(0,password)
   




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
        with open('data.json','w') as data_file:
            json.dump(new_data, data_file)
            web_entry.delete(0,END)
            pwd_entry.delete(0,END) 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passcode Manager")
window.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website = Label(text='Website:')
website.grid(column=0,row=1)
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(column=1,row=1, columnspan=2)

user = Label(text='Username/Email:')
user.grid(column=0,row=2)
user_entry = Entry(width=35)
user_entry.insert(END, 'nikhilshetty00@gmail.com')
user_entry.grid(column=1,row=2, columnspan=2)

pwd = Label(text='Password:')
pwd.grid(column=0,row=3)
pwd_entry = Entry(width=21)
pwd_entry.grid(column=1,row=3,columnspan=2)

pwd_gen = Button(text="Generate Password",command=gen_pass)
pwd_gen.grid(column=3,row=3)

add_but = Button(text='Add', width=36, command=pass_save)
add_but.grid(column=1,row=4,columnspan=2)




window.mainloop()