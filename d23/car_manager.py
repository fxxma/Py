from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

CAR_POS = [i for i in range(-280,280,20)]

class CarManager():
    
    def __init__(self) -> None:
        self.cars = []
    
    