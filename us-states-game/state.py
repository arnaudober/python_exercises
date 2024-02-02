from turtle import Turtle

class State(Turtle):
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def draw(self):
        turtle = Turtle("blank")
        turtle.speed("fastest")
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.write(self.state)
