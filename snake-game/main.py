from turtle import Screen
from snake import *
from food import *
from scoreboard import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    board.write_score()
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        board.increase_score()

    hit_horizontal_wall = snake.head.xcor() > 280 or snake.head.xcor() < -280
    hit_vertical_wall = snake.head.ycor() > 280 or snake.head.ycor() < -280
    if hit_horizontal_wall or hit_vertical_wall:
        game_is_on = False
        board.game_over()

screen.exitonclick()
