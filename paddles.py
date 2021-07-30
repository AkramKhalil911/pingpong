from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(location)

    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -225:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)