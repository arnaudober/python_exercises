from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def go_clockwise():
    turtle.setheading(turtle.heading() + 10)


def go_counter_clockwise():
    turtle.setheading(turtle.heading() - 10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(move_forward, "Right")
screen.onkey(move_backward, "Left")
screen.onkey(go_counter_clockwise, "a")
screen.onkey(go_clockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()
