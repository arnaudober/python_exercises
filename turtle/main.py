from turtle import Turtle

turtle = Turtle()

# Draw a square
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)


# Draw a dashed line


turtle.penup()
turtle.goto(-200, 0)


def motion():
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)


for i in range(10):
    motion()

turtle.screen.mainloop()
