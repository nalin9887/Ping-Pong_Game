from turtle import Turtle
self=Turtle()
move=40

class Paddle(Turtle):

      def __init__(self,posiiton_x,position_y):
            super().__init__()
            self.shape("square")
            self.color("white")
            self.shapesize(5, 1)
            self.penup()
            self.goto(posiiton_x, position_y)


      def move_up(self):
            new_y=self.ycor()+move
            self.goto(self.xcor(), new_y)
      def move_down(self):
             new_y=self.ycor()-move
             self.goto(self.xcor(), new_y)







