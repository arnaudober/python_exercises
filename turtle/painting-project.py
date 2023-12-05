import random
from turtle import *

import colorgram

colors = colorgram.extract("image.jpg", 30)

turtle = Turtle()
turtle.speed("fastest")
turtle.hideturtle()
colormode(255)

turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
count = 100

for i in range(1, count + 1):
    color = random.choice(colors)
    turtle.pendown()
    turtle.dot(20, color.rgb)
    turtle.penup()
    turtle.forward(50)

    if i % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

turtle.screen.mainloop()
