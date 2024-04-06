import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onclick(player.move_up(),"Up")
screen.onclick(player.move_down(),"Down")
screen.onclick(player.move_right(),"Right")
screen.onclick(player.move_left(),"Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()