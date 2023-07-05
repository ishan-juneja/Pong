from turtle import Turtle


class Score(Turtle):
    score_counter = 0

    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.setposition(x, y)
        self.pendown()
        self.color("white")
        self.write(f"{self.score_counter}", font=("Arial", 20, "normal"), align="center")

    def increment(self):
        self.score_counter += 1
        self.clear()
        self.write(self.score_counter, font=("Arial", 20, "normal"), align="center")

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over!", font=("Arial", 20, "normal"), align="center")
