from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.high_score = data.read()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updated_score()

    def updated_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.updated_score()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.updated_score()

