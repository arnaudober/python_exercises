from turtle import Screen
from pandas import read_csv
from state import *

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

# Initialize the states
all_states = []
data = read_csv("50_states.csv")
for i in data.index:
    state = State(x=data['x'][i], y=data['y'][i], state=data['state'][i])
    all_states.append(state)
    
all_states_count = len(all_states)
guessed_states = []

while len(guessed_states) < all_states_count:
    guessed_states_count = len(guessed_states)
    answer = screen.textinput(title=f"{guessed_states_count} States Correct", prompt="What's another state's name?").title()
    if answer == "Exit":
        break
    
    for state in all_states:
        if state.state == answer and state.state not in guessed_states:
            state.draw()
            guessed_states.append(state.state)
            break

# If we exited, we didn't for sure guess all the states
if len(guessed_states) == all_states_count:
    turtle = Turtle("blank")
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.write("You've guessed all the states!", align="center", font=("Arial", 24, "normal"))
    screen.exitonclick()

