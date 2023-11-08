from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pace = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.cars = []
        self.generate()
        self.refresh()
    
        
    def generate(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(r.choice(COLORS))
        car.goto(x=300, y=r.randint(-250, 250))
        self.cars.append(car)
    
    def move(self):
        for car in self.cars:
            car.forward(self.pace)
    
    def refresh(self):
        for car in self.cars:
            if car.xcor() < -300:
                self.cars.remove(car)
