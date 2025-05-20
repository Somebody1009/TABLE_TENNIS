from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.move_speed = 20

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + self.move_speed)

    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - self.move_speed)

    def bind_controls(self, screen, up_key, down_key):
        screen.onkey(self.go_up, up_key)
        screen.onkey(self.go_down, down_key)