import turtle
import time
from logging.config import listen
import ball
from scoreboard import Scoreboard

import paddle


screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height = 600)
screen.title("Pong")
screen.tracer(0)
paddle_r = paddle.Paddle((350, 0))
paddle_l = paddle.Paddle((-350, 0))
ball = ball.Ball()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
#Commands for the RIGHT PADDLE
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
#Commands for the LEFT PADDLE
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()


    # Detecting collision with paddle
    if ball.distance(paddle_r)<50 and ball.xcor() > 320 or ball.distance(paddle_l)<50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    # Detecting balls out of bounds
    if ball.xcor() > 380:
        ball.goto(0,0)
        ball.bounce_x()
        scoreboard.l_point()
        ball.move_speed = 1
    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.bounce_x()
        scoreboard.r_point()
        ball.move_speed = 1










screen.exitonclick()
