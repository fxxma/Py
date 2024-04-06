from turtle import Turtle

class Paddle(Turtle) :

    def __init__(self,coor) :
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5.0,1.0,None)
        self.color("white")
        self.goto(coor)
    
    def go_up(self) :
        new_y = self.ycor() + 40
        self.goto(self.xcor(),new_y)

    def go_down(self) :
        new_y = self.ycor() - 40
        self.goto(self.xcor(),new_y)

