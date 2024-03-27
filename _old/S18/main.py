import turtle as t
import random as r

tim = t.Turtle()
opt = [tim.right,tim.left,tim]

for _ in range(50) :
    opt[r.randint(0,1)](90*r.randint(0,1))
    tim.forward(10)
    


screen = t.Screen()
screen.exitonclick()