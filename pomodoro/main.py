from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    global timer
    reps = 0

    root.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canva.itemconfig(countdown_label, text="00:00")
    check_icon.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_countdown():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time
import math

def count_down(count):
    global timer

    if count >= 0:
        timer = root.after(1000, count_down, count - 1)
        minutes = math.floor(count / 60)
        seconds = count % 60
        if seconds <= 9:
            seconds = f"0{seconds}"

        canva.itemconfig(countdown_label, text=f"{minutes}:{seconds}")
    else:
        start_countdown()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_icon.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Podomoro")
root.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

canva = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canva.create_image(100, 112, image=image)
countdown_label = canva.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canva.grid(column=1, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_countdown)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

check_icon = Label(fg=GREEN, bg=YELLOW)
check_icon.grid(column=1, row=3)

root.mainloop()