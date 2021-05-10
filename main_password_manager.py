from tkinter import *
from tkinter import messagebox
import random
import json
GREY = "#DCDCDC"

#Password Generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    print(f"Your password is: {password}")


#Saving data to file

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:
            {
                "email": email,
                "password": password,
            }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS",message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("data.json","r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=3)
        else:
            #Updating new data with old data
            data.update(new_data)
            with open("data.json","w") as data_file:
                #Writing data
                json.dump(data,data_file, indent=3)
        finally:
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0,END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="This data does not exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")


window =Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg=GREY)

canvas = Canvas(width = 225, height = 225,bg=GREY,highlightthickness=0)
image = PhotoImage(file="images-removebg-preview.png")
canvas.create_image(111,111,image=image)
canvas.grid(column=1,row=0)

#Labels
website_label = Label(text="Website: ",font = ("Aerial",12,"normal"),bg=GREY)
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username: ",font = ("Aerial",12,"normal"),bg=GREY)
email_label.grid(column=0,row=2)

password_label = Label(text="Password: ",font = ("Aerial",12,"normal"),bg=GREY)
password_label.grid(column=0,row=3)

#Entry
website_entry = Entry(width = 35)
website_entry.grid(column=1,row=1)
website_entry.focus()

email_entry = Entry(width = 35)
email_entry.grid(column=1,row=2)

password_entry = Entry(width = 35)
password_entry.grid(column=1,row=3)

#Buttons
generate_password = Button(text="Generate Password",width=25,command = generate_password)
generate_password.grid(column=2,row=3)

add_password = Button(text="Add",width=30, command = save)
add_password.grid(column=1,row=4)

search_button = Button(text="Search",width=25, command = find_password)
search_button.grid(column=2,row=1)
window.mainloop()