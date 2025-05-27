from turtle import Turtle
from interface import declare_winner

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # Player A – ліворуч
        self.goto(-250, 260)
        self.write(f"Player A: {self.l_score}", align="left", font=("Courier", 14, "normal"))
        # Player B – праворуч
        self.goto(150, 260)
        self.write(f"Player B: {self.r_score}", align="left", font=("Courier", 14, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
        self.check_winner()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
        self.check_winner()

    def check_winner(self):
        if self.l_score >= 5:
            declare_winner("Player A")
        elif self.r_score >= 5:
            declare_winner("Player B")

    def show_final_score(self):
        self.goto(0, 0)
        self.write(f"Final Score:\nPlayer A: {self.l_score} | Player B: {self.r_score}", align="center", font=("Courier", 20, "bold"))
