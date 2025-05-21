from turtle import Turtle
import time
import random

status_writer = Turtle()
status_writer.hideturtle()
status_writer.color("white")
status_writer.penup()

speed_writer = Turtle()
speed_writer.hideturtle()
speed_writer.color("white")
speed_writer.penup()
speed_writer.goto(-280, 235)

speed_label = Turtle()
speed_label.hideturtle()
speed_label.color("gray")
speed_label.penup()
speed_label.goto(-380, 230)
speed_label.write("SPEED", align="left", font=("Courier", 16, "bold"))

bounce_writer = Turtle()
bounce_writer.hideturtle()
bounce_writer.color("white")
bounce_writer.penup()
bounce_writer.goto(0, 235)

bounce_label = Turtle()
bounce_label.hideturtle()
bounce_label.color("gray")
bounce_label.penup()
bounce_label.goto(-130, 230)
bounce_label.write("BOUNCES", align="left", font=("Courier", 16, "bold"))

timer_writer = Turtle()
timer_writer.hideturtle()
timer_writer.color("white")
timer_writer.penup()
timer_writer.goto(280, 235)

timer_label = Turtle()
timer_label.hideturtle()
timer_label.color("gray")
timer_label.penup()
timer_label.goto(200, 230)
timer_label.write("TIME", align="left", font=("Courier", 16, "bold"))

start_time = time.time()
bounce_count = 0

def update_speed_display(speed):
    speed_writer.clear()
    speed_writer.write(f"{speed:.2f}", align="left", font=("Courier", 14, "normal"))

def update_bounce_display():
    bounce_writer.clear()
    bounce_writer.write(f"{bounce_count}", align="left", font=("Courier", 14, "normal"))

def update_timer_display():
    elapsed = int(time.time() - start_time)
    minutes = elapsed // 60
    seconds = elapsed % 60
    timer_writer.clear()
    timer_writer.write(f"{minutes:02d}:{seconds:02d}", align="left", font=("Courier", 14, "normal"))

def register_bounce():
    global bounce_count
    bounce_count += 1
    update_bounce_display()