from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


def get_high_score():
    with open("data.txt") as data:
        return int(data.read())


def set_high_score(high_score):
    with open("data.txt", "w") as data:
        data.write(str(high_score))


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            set_high_score(self.score)
        self.score = 0
        self.update_score()
