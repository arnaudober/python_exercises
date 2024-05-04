from tkinter import *
from tkinter import messagebox

DEFAULT_EMAIL = 'me@arnaudober.com'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

# 1. Logo
canva = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canva.create_image(100, 100, image=image)
canva.grid(row=0, column=1)

# 2. Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="E")

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

# 3. Email/Username
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0, sticky="E")

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_username_entry.insert(0, DEFAULT_EMAIL)

# 4. Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

# 5. Add Button

def add():
  website = website_entry.get()
  email = email_username_entry.get()
  password = password_entry.get()

  is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                         f"Email: {email}\n"
                         f"Password: {password}\n"
                         f"Is it ok to save?")

  if is_ok:
    with open('data.txt', 'a') as file:
      file.write(f"{website}\t | \t{email}\t | \t{password}\n")

    website_entry.delete(0, END)
    email_username_entry.delete(0, END)
    email_username_entry.insert(0, DEFAULT_EMAIL)
    password_entry.delete(0, END)


add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()