from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'bold')
STARTING_POSITION = (0,260)

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(STARTING_POSITION)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()