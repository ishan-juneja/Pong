from turtle import Turtle
import random

class Paddle(Turtle):
    paddle_speed = 5

    def __init__(self, position_tuple, paddle_speed):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(0)
        self.shapesize(1, 4)
        self.penup()
        self.left(90)
        self.goto(position_tuple)
        self.paddle_speed = paddle_speed

    def chase(self, ball, height):
        temp = random.randint(0,9)
        if temp <= 5:
            if self.ycor() < height - 20:
                if ball.ycor() >= (self.ycor() + 10):
                    self.up()
                elif ball.ycor() <= (self.ycor() - 10):
                    self.down()

            if self.ycor() > -height + 20:
                if ball.ycor() >= (self.ycor() + 10):
                    self.up()
                elif ball.ycor() <= (self.ycor() - 10):
                    self.down()
            else:
                self.up()

    def up(self):
        self.forward(self.paddle_speed)

    def down(self):
        self.backward(self.paddle_speed)
