from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canva = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canva.create_image(100, 100, image=image)
canva.pack()

window.mainloop()