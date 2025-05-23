from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from interface import setup_menu, is_running, is_paused, register_bounce, update_timer_display, update_speed_display
import time
import random

LEVEL = 0
NUM_BALLS = 0
balls = []
recent_bounces = []

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

selector = Turtle()
selector.hideturtle()
selector.color("white")
selector.penup()
selector.goto(0, 0)
selector.write("Вибери рівень: [1], [2], або [3]", align="center", font=("Courier", 20, "normal"))

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()

def start_level(level):
    global LEVEL, NUM_BALLS, balls, recent_bounces
    LEVEL = level
    NUM_BALLS = LEVEL
    selector.clear()

    balls = [Ball() for _ in range(NUM_BALLS)]
    start_x, start_y = 0, 0
    balls[0].goto(start_x, start_y)
    for i in range(1, NUM_BALLS):
        balls[i].goto(start_x, start_y)
        balls[i].x_move = random.choice([-1, 1]) * (2 + random.random() * 2)
        balls[i].y_move = random.choice([-1, 1]) * (2 + random.random() * 2)

    recent_bounces = [False] * NUM_BALLS

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    setup_menu(screen, balls[0], scoreboard)
    run_game()

def run_game():
    game_is_on = True
    try:
        while game_is_on:
            screen.update()

            if not is_running() or is_paused():
                continue

            time.sleep(balls[0].move_speed)
            for i, ball in enumerate(balls):
                ball.move()
                update_timer_display()
                update_speed_display(ball.move_speed)

                if -320 < ball.xcor() < 320:
                    recent_bounces[i] = False

                if not recent_bounces[i] and (
                        (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or
                        (ball.distance(l_paddle) < 50 and ball.xcor() < -320)
                ):
                    ball.bounce_x()
                    register_bounce()
                    recent_bounces[i] = True

                if ball.ycor() > 280 or ball.ycor() < -280:
                    ball.bounce_y()
                    register_bounce()

                if abs(ball.xcor()) > 380:
                    if ball.xcor() > 0:
                        scoreboard.l_point()
                    else:
                        scoreboard.r_point()
                    ball.reset_position()
                    ball.goto(0, 0)
                    ball.x_move = random.choice([-1, 1]) * (2 + random.random() * 2)
                    ball.y_move = random.choice([-1, 1]) * (2 + random.random() * 2)

    except:
        print("Гру завершено вручну.")

screen.listen()
screen.onkey(lambda: start_level(1), "1")
screen.onkey(lambda: start_level(2), "2")
screen.onkey(lambda: start_level(3), "3")

screen.mainloop()