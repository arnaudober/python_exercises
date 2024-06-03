import random
import time
from tkinter import Button, Canvas, Label, PhotoImage, Tk

import pandas


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

# Read data
try:
  data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  data = pandas.read_csv("data/french_words.csv")
except pandas.errors.EmptyDataError:
  data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")

current_card = {}

# Functions
def save_progress():
  data_dict.remove(current_card)
  data = pandas.DataFrame(data_dict)
  data.to_csv("data/words_to_learn.csv", index=False)
  next_card()

def next_card():
  global current_card, flip_timer

  window.after_cancel(flip_timer)
  current_card = random.choice(data_dict)
  canva.itemconfig(image_item, image=card_front_image)
  canva.itemconfig(title_label, text="French", fill="black")
  canva.itemconfig(word_label, text=current_card['French'], fill="black")
  flip_timer = window.after(3000, flip_card)

def flip_card():
  canva.itemconfig(image_item, image=card_back_image)
  canva.itemconfig(title_label, text="English", fill="white")
  canva.itemconfig(word_label, text=current_card['English'], fill="white")

# Trick to get a mock flip_timer to cancel when next_card is called
flip_timer = window.after(3000, flip_card)

# Canvas
canva = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_item = canva.create_image(400, 263, image=card_front_image)

title_label = canva.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_label = canva.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

canva.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, border=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, border=0, command=save_progress)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
