from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

p1 = Paddle((350,0))
p2 = Paddle((-350,0))

b = Ball()

scoreboard = Scoreboard()
screen.listen()

screen.onkey(p1.go_up,"Up")
screen.onkey(p1.go_down,"Down")

screen.onkey(p2.go_up,"w")
screen.onkey(p2.go_down,"s")

is_on = True
while is_on :
    time.sleep(0.1)
    screen.update()
    b.move()

    if abs(b.ycor()) > 280:
        b.bounce_y()
    
    #detect collision with p1
    if  (b.distance(p1) < 50 and b.xcor() > 340) or (b.distance(p2) < 50 and b.xcor() < -340): 
        b.bounce_x()
    
    if b.xcor() > 380 :
        b.reset()

    if b.xcor() < 380 :
        b.reset()



screen.exitonclick()
