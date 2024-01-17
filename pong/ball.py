from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)
        self.x_move = 10
        self.y_move = 10
        self.current_speed = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()

    def reset_pos(self):
        self.goto(x=0, y=0)
        self.reset_speed()
        self.bounce_x()

    def reset_speed(self):
        self.current_speed = 1
        self.speed(self.current_speed)

    def increase_speed(self):
        self.current_speed *= 0.9
