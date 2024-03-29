import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.up, "Up")

scoreboard = Scoreboard()

car_manager = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.print_level()

    car_manager.create_car()
    car_manager.move()

    if car_manager.detect_collision(player):
        scoreboard.game_over()
        game_is_on = False
        
    if player.has_reached_other_side():
        player.go_to_start()
        car_manager.speed_up()
        scoreboard.increase_level()

screen.exitonclick()
