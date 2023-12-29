from random import randint
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

winning_turtle = None
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y = -100
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=y)
    y = y + 40
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            break

        turtle.forward(randint(0, 10))

if winning_turtle == user_bet:
    print(f"You won! The turtle who won the race was {winning_turtle}.")
else:
    print(f"You lost! The turtle who won the race was {winning_turtle}.")

screen.exitonclick()
