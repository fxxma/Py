from turtle import *
from random import *


is_race_on = False
screen = Screen()
screen.setup(width= 500,height= 400)
user_input = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color:")
colors = ["red","orange","yellow","green","blue","purple"]
y_index = [-100,-50,0,50,100,150]
all_turtles = []

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_index[i])
    all_turtles.append(new_turtle)

if user_input :
    is_race_on = True

while is_race_on :
    for turtle in all_turtles :
        if turtle.xcor() >= screen.window_width()/2 :
            if user_input == turtle.pencolor() :
                print("Congratz you win!")
            else :
                print("Boo you suck!")
            is_race_on = False
        rand_dist = randint(0,10) 
        turtle.forward(rand_dist)

screen.exitonclick()