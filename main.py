import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(tim.move, "w")

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    cars.move()
    screen.update()
    
    counter += 1
    if cars.pace == 5:
        if counter == 5:
            cars.generate()
            counter = 0
    else:
        if counter == 3:
            cars.generate()
            counter = 0
    
    for car in cars.cars:
        if tim.distance(car) < 25:
            tim.game_over()
            game_is_on = False
    
    if tim.is_at_finish_line():
        tim.goto(STARTING_POSITION)
        cars.pace += MOVE_INCREMENT
        scoreboard.increase_level()
        

screen.exitonclick()