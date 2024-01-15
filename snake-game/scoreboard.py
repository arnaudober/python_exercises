from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def write_score(self):
        self.write("Score: 0", align="center", font=("Arial", 24, "normal"))

