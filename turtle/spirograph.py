from random import randint
from turtle import *

turtle = Turtle()
turtle.speed("fastest")
colormode(255)


def random_color():
    return [randint(0, 255), randint(0, 255), randint(0, 255)]


def draw_spirograph(size):
    for i in range(int(360 / size)):
        rgb = random_color()
        turtle.pencolor(rgb[0], rgb[1], rgb[2])
        turtle.circle(100)
        turtle.left(size)


draw_spirograph(2)
turtle.screen.mainloop()
