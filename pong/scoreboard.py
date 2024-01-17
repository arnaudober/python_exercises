from turtle import Turtle

FONT = ("Courier", 80, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def write_score(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.l_score, align=ALIGN, font=FONT)

        self.goto(x=100, y=200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def add_point_to_paddle(self, paddle):
        if paddle == "left":
            self.l_score += 1
        else:
            self.r_score += 1

