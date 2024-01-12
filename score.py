from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.ht()
        self.penup()
        self.color("White")
        self.l_score=0
        self.r_score=0
        self.goto(0,270)
        self.write(f"{self.l_score}  ||   {self.r_score}",align="center",font=("Verdana",
                                    18, "bold"))

    def rscoreplu(self):
        self.r_score+=1
        self.clear()
        self.write(f"{self.l_score}  ||   {self.r_score}",align="center",font=("Verdana",
                                    18, "bold"))
    def lscoreplus(self):
        self.l_score+=1
        self.clear()
        self.write(f"{self.l_score}  ||   {self.r_score}",align="center",font=("Verdana",
                                    18, "bold"))


    def gameover(self):
        self.goto(0,0)
        self.color("Red")
        self.write("GameOVER!!!!!",align="center",font=("Verdana",
                                    25, "bold"))
