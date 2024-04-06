from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("purple")
        self.shape("square")
        self.goto(STARTING_POSITION)
    
    def move_up(self) :
        self.forward(MOVE_DISTANCE)
    
    def move_down(self) :
        self.back(MOVE_DISTANCE)
    
    def move_right(self) :
        self.right(MOVE_DISTANCE)

    def move_left(self) :
        self.left(MOVE_DISTANCE)