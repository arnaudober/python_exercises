from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# In that order so the drawing looks smooth
starting_pos = [(0, 0), (-20, 0), (-40, 0)]

for pos in starting_pos:
    segment = Turtle()
    segment.shape("square")
    segment.color("white")
    segment.goto(x=pos[0], y=pos[1])

screen.exitonclick()