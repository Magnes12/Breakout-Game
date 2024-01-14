import turtle
import time
from paddle import Paddle
from ball import Ball
from bricks import Bricks


def main():
    screen = turtle.Screen()
    screen.bgcolor('black')
    screen.setup(width=800,height=600)
    screen.title('Breakout')
    screen.tracer(0)

    player_paddle = Paddle()
    ball = Ball()

    bricks_instance = Bricks(-140, 200)
    bricks = bricks_instance.bricks_create()

    screen.listen()
    screen.onkey(player_paddle.moveleft, "a")
    screen.onkey(player_paddle.moveright, "d")

    def update_game():
        screen.update()
        ball.move()

        if ball.ycor() > 280:
            ball.bounce_y()

        if ball.ycor() < -280:
            time.sleep(2)
            turtle.bye()

        if ball.distance(player_paddle) < 20 and ball.ycor() < 280:
            ball.bounce_y()

        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()

        # Detect bricks collision

        screen.ontimer(update_game, 100)

    update_game()

    turtle.done()

if __name__ == "__main__":
    main()