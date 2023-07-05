from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
# Screen Setup
main_Screen = Screen()
main_Screen.setup(width=800, height=500)
main_Screen.bgcolor("black")
main_Screen.tracer(0)

# Dashed Turtles for Screen Setup
dash_turtle = Turtle()
dash_turtle.hideturtle()
dash_turtle.speed(0)
dash_turtle.penup()
dash_turtle.goto(0, -250)
dash_turtle.setheading(90)
dash_turtle.width(4)
dash_turtle.color("white")
for i in range(0, 50):
    dash_turtle.pendown()
    dash_turtle.forward(5)
    dash_turtle.penup()
    dash_turtle.forward(10)

#Creating user paddle
user_paddle = Paddle(position_tuple=(-375,0), paddle_speed=22)
#Creating NPC paddle
computer_paddle = Paddle(position_tuple=(375,0), paddle_speed=20)

#Creating ball
game_ball = Ball(screen_height=250, ball_speed=15)
game_ball.reposition(250)

#creating scorecounter
user_score = Score(-10,220)
computer_score = Score(10,220)

game_condition = True

while game_condition:
    game_ball.speed()
    #collision detection for ball
    if(game_ball.distance(user_paddle) <= 30 or game_ball.distance(computer_paddle)<= 30):
        game_ball.paddleCollision()
        game_ball.increment_ball_speed()
        game_ball.move()
    game_ball.wallCollision(screen_height=250)
    if game_ball.xcor()<= -400:
        time.sleep(0.25)
        computer_score.increment()
        game_ball.reset(x=15,y=15,screen_height=250)
    if game_ball.xcor()>= 400:
        time.sleep(0.25)
        user_score.increment()
        game_ball.reset(x=15, y=15, screen_height=250)




    game_ball.move()

    #computer chase
    computer_paddle.chase(game_ball, height=250)


    #user paddle movement

    main_Screen.onkey(fun=user_paddle.up, key="w")
    main_Screen.onkeypress(fun=user_paddle.up, key="w")
    main_Screen.onkey(fun=user_paddle.down, key="s")
    main_Screen.onkeypress(fun=user_paddle.down, key="s")
    main_Screen.listen()





    time.sleep(0.05)

    main_Screen.update()

game_condition = False





main_Screen.exitonclick()