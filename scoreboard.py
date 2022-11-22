from turtle import Turtle


ALIGN = "center"
FONT = ('arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over.", align=ALIGN, font=('arial', 40, 'normal'))

    def increase_score(self):
        self.score += 100
        self.clear()
        self.update_score()
