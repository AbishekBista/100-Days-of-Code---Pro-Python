from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.high_score = 0
        with open('highscore_data.txt') as file:
            score_content = int(file.read())
            self.high_score = score_content

        self.render_score()

    def render_score(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High score: {self.high_score}', align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore_data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        