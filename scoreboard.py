from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


def read_high_score():
    with open("data.txt") as file:
        score = file.read()
        return int(score)


def write_high_score(content):
    with open("data.txt", mode="w") as file:
        file.write(str(content))



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_amount = 0
        read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_amount} High Score : {read_high_score()}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score_amount > read_high_score():
            # self.high_score = self.score_amount
            write_high_score(self.score_amount)
        self.score_amount = 0
        self.update_scoreboard()

    def add_score(self):
        self.score_amount += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
