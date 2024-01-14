import turtle

class Paddle(turtle.Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=7)
        self.setposition(0, -250)
    
    def moveright(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def moveleft(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())  
