from turtle import Screen
from paddle import *
from ball import *
from scoreboard import *
import time

# Screen
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddles
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

# Ball
ball = Ball()

# Score board
score_board = ScoreBoard()

game_is_on = True
while game_is_on:
    score_board.write_score()

    screen.update()
    time.sleep(ball.current_speed / 100)
    ball.move()

    # Collisions detection
    touches_top_or_bottom_wall = ball.ycor() > 280 or ball.ycor() < -280
    if touches_top_or_bottom_wall:
        ball.bounce_y()

    touches_right_paddle = paddle1.distance(ball) < 50 and ball.xcor() > 320
    touches_left_paddle = paddle2.distance(ball) < 50 and ball.xcor() < -320
    if touches_right_paddle or touches_left_paddle:
        ball.bounce_x()
        print(ball.current_speed)

    ball_is_beyond_right_paddle = ball.xcor() > 380
    ball_is_beyond_left_paddle = ball.xcor() < -380
    if ball_is_beyond_right_paddle:
        ball.reset_pos()
        score_board.add_point_to_paddle("left")
    elif ball_is_beyond_left_paddle:
        ball.reset_pos()
        score_board.add_point_to_paddle("right")

screen.exitonclick()
