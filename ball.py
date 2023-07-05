from turtle import Turtle
import random
class Ball(Turtle):
    x_speed = 5
    y_speed = 5

    def __init__(self, screen_height, ball_speed):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(0.5,0.5)
        self.x_speed = -ball_speed
        self.y_speed = ball_speed
        self.reposition(screen_height)

    def reposition(self, screen_height):
        y = random.randint((-screen_height + 20), (screen_height - 20))
        self.setposition(0, y)

    def move(self):
        self.setheading(0)
        self.forward(self.x_speed)
        self.setheading(90)
        self.forward(self.y_speed)

    def wallCollision(self, screen_height):
        if(self.ycor()+5 >= screen_height or self.ycor()-5 <= -screen_height ):
            self.y_speed = -self.y_speed
            self.move()

    def increment_ball_speed(self):
        temp = random.randint(0,15)/100
        self.x_speed = self.x_speed * (1 + temp)
        self.y_speed = self.y_speed * (1 + temp)

    def reset(self,x,y,screen_height):
        self.x_speed = x
        self.y_speed = y
        self.reposition(screen_height)


    def paddleCollision(self):
        self.x_speed = -self.x_speed
        # self.y_speed = -self.y_speed



