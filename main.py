from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Ping, pong")
screen.tracer(0)

player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.score()
screen.listen()
screen.onkeypress(player_1.up, "w")
screen.onkeypress(player_1.down, "s")
screen.onkeypress(player_2.up, "Up")
screen.onkeypress(player_2.down, "Down")

isTrue = True
while isTrue == True:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if ball.distance(player_1.pos()) < 50 and ball.xcor() == -340 or ball.distance(player_2.pos()) < 50 and ball.xcor() == 340:
        ball.bounce_x()
    elif ball.xcor() == 380:
        ball.reset_position()
        scoreboard.player1_scores()
    elif ball.xcor() == -380:
        ball.reset_position()
        scoreboard.player2_scores()


screen.exitonclick()
