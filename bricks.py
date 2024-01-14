import turtle

class Bricks(turtle.Turtle):

    def __init__(self, x, y) -> None:
        super().__init__()
        self.shape('square')
        self.color('red')
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=3)
        self.goto(x, y)

    def bricks_create(self):
        bricks = []
        brick_spacing_x = 70
        brick_spacing_y = 30

        for row in range(5):
            for col in range(5):
                brick = Bricks(-140 + col * brick_spacing_x, 200 - row * brick_spacing_y)
                bricks.append(brick)

        return bricks
