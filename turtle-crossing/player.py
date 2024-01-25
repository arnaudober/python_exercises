from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.go_to_start()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def has_reached_other_side(self):
        return self.ycor() > FINISH_LINE_Y
    
    def go_to_start(self):
        self.penup()
        self.setposition(STARTING_POSITION)
