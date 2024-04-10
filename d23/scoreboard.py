from turtle import Turtle

FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-270,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align="left",font = FONT)

    def game_over(self) :
        self.write("Game Over",align= "center",font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
