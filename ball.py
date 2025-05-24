from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 4
        self.y_move = 4
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()
        from turtle import Turtle
        import random

        class Ball(Turtle):

            def __init__(self):
                super().__init__()
                self.color("white")
                self.shape("circle")
                self.penup()
                self.x_move = random.choice([-1, 1]) * (2 + random.random() * 2)
                self.y_move = random.choice([-1, 1]) * (2 + random.random() * 2)
                self.move_speed = 0.05
                self.update_color()

            def move(self):
                new_x = self.xcor() + self.x_move
                new_y = self.ycor() + self.y_move
                self.goto(new_x, new_y)
                self.update_color()

            def bounce_y(self):
                self.y_move *= -1
                self.slow_down()

            def bounce_x(self):
                self.x_move *= -1
                self.move_speed *= 0.9
                self.update_color()

            def reset_position(self):
                self.goto(0, 0)
                self.move_speed = 0.1
                self.bounce_x()

            def slow_down(self):
                self.move_speed *= 1.05

            def update_color(self):
                if self.move_speed < 0.03:
                    self.color("red")
                elif self.move_speed < 0.07:
                    self.color("orange")
                else:
                    self.color("white")