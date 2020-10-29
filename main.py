from snake import *

if __name__ == "__main__":
    turtle.setup(500,500)

    turtle.tracer(0)
    turtle.hideturtle()
    turtle.listen()
    turtle.onkey(lambda: change_direction(0,10),"Up")
    turtle.onkey(lambda: change_direction(0,-10),"Down")
    turtle.onkey(lambda: change_direction(-10,0),"Left")
    turtle.onkey(lambda: change_direction(10,0),"Right")

    snake_move()
    turtle.done()

