from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")



class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align = ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.write_score()


    def increase_score(self):
        self.score += 1
        self.write_score()