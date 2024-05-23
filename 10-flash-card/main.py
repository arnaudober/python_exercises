import random
from tkinter import Button, Canvas, Label, PhotoImage, Tk

import pandas


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Read data
data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")

# Functions
def next_card():
  current_card = random.choice(data_dict)
  canva.itemconfig(title_label, text="French", fill="black")
  canva.itemconfig(word_label, text=current_card['French'], fill="black")

# Canvas
canva = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="images/card_front.png")
canva.create_image(400, 263, image=image)

title_label = canva.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_label = canva.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

canva.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, border=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, border=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
