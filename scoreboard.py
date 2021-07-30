from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.score()

    def score(self):
        self.reset()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 200)
        self.write(f"{self.player1_score}", align="center", font=("Arial", 50, "normal"))
        self.goto(100, 200)
        self.write(f"{self.player2_score}", align="center", font=("Arial", 50, "normal"))

    def player1_scores(self):
        self.player1_score += 1
        self.score()

    def player2_scores(self):
        self.player2_score += 1
        self.score()