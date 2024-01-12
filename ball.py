from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Blue")
        self.penup()
        self.x_mvoe=10
        self.y_move=10

    def ball_move(self):
        new_x=self.xcor()+self.x_mvoe
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move*=-1
    def paddle_bounce(self):
        self.y_move*=-1
        self.x_mvoe*=-1
