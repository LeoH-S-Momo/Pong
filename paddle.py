import turtle

class Paddle(turtle.Turtle):

    def __init__(self, position):

        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

#Question left unanswered:
#In this code, when initializing the object, instead of the code I have here, I used
    # def __init__(self, position):
    #
    #     super().__init__()
    #     self.paddle1.shape("square")
    #     self.paddle1.color("white")
    #     self.paddle1.shapesize(stretch_wid=5, stretch_len=1)
    #     self.paddle1.penup()
    #     self.paddle1.goto(position)
#And the code stopped working completely, there was no subsequent collision with the paddles, why is that?
