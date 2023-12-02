import random
from turtle import *

turtle = Turtle()
turtle.pensize(15)
turtle.speed("fastest")
angles = [0, 90, 180, 270]
colormode(255)

for i in range(200):
    rgb = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    turtle.pencolor(rgb[0], rgb[1], rgb[2])
    turtle.forward(30)
    turtle.setheading(random.choice(angles))

turtle.screen.mainloop()
