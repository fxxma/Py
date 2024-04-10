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
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")
screen.onkey(player.move_right,"Right")
screen.onkey(player.move_left,"Left")

carmanager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.add_car()
    carmanager.move_car()
    player.forward(50)
    if player.ycor() > player.finishline :
        scoreboard.increase_score()
        # player.goto(player.starting_pos)
        carmanager.reset()
        carmanager.speed += 1


screen.exitonclick()