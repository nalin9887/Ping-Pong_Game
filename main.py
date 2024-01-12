from turtle import Turtle,Screen
from paddle import Paddle
from score import Score
import time
from ball import Ball

score=Score()
ball=Ball()
screen=Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("PING-PONG")
screen.tracer(0)

tim_r=Paddle(350,0)
tim_l=Paddle(-350,0)



screen.listen()
screen.onkey(tim_l.move_up,"w")
screen.onkey(tim_l.move_down,"s")
screen.onkey(tim_r.move_up,"Up")
screen.onkey(tim_r.move_down,"Down")


gameison=True
while gameison:
    time.sleep(0.1-0.05)
    screen.update()
    ball.ball_move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    if ball.distance(tim_l)<50:
        ball.paddle_bounce()
        score.lscoreplus()

    if ball.distance(tim_r)<50:
        ball.paddle_bounce()
        score.rscoreplu()
    if ball.xcor()>390:
        score.gameover()
        gameison=False


screen.exitonclick()
