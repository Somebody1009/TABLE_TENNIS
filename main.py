from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from interface import setup_menu, is_running, is_paused, register_bounce, update_timer_display, update_speed_display
import time
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

setup_menu(screen, ball, scoreboard)

game_is_on = True
while game_is_on:
    screen.update()

    if not is_running() or is_paused():
        continue

    time.sleep(ball.move_speed)
    ball.move()
    update_timer_display()
    update_speed_display(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        register_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        register_bounce()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        register_bounce()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.mainloop()
