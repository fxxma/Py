from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

SUCC = 10 
ODDS = [1 for i in range(SUCC)] + [0 for i in range(10-SUCC)]
CAR_POS = [i for i in range(-260,260,20)]

class CarManager():
    
    def __init__(self) -> None:
        self.cars = []
        self.speed = 1

    class Car(Turtle) :
        def __init__(self) :
            super().__init__()
            self.penup()
            self.shape("square")
            self.color(COLORS[random.randint(1,len(COLORS))-1])
            self.shapesize(stretch_wid=1,stretch_len=2)
            self.goto(300,CAR_POS[random.randint(1,len(CAR_POS))-1])

    def add_car(self) :
        if random.randint(1,len(ODDS))-1 == 1 :
            self.cars.append(CarManager.Car())
        else :
            pass

    def move_car(self) :
        for car in self.cars :
            car.goto(car.xcor() - STARTING_MOVE_DISTANCE*self.speed,car.ycor())

    def reset(self) :
        for car in self.cars :
            car.undo()
            car.reset()
        self.cars = []
