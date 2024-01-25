from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 5:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            color = random.choice(COLORS)
            car.color(color)
            car.setheading(180)
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_speed)

    def detect_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
            
        return False
    
    def speed_up(self):
        self.move_speed += MOVE_INCREMENT