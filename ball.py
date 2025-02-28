import turtle
from turtle import Turtle


class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.X = 10
        self.Y = 10
        self.move_speed = 1

    def move(self):
        new_x = self.xcor() + self.X * self.move_speed
        new_y = self.ycor() + self.Y
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.Y *= -1

    def bounce_x(self):
        self.X *= -1

    def increase_speed(self):
        self.move_speed += 0.5
