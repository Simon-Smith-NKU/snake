import turtle
import copy
from random import randrange
from tkinter import messagebox
points = 0
snakes = [[0,0],[0,10],[0,20]]
aim = [0,10]
food = [-10,0]
barriers = []
new_barrier = [0,0]
#此处必须全部预置完毕

def inside(head):
    return(head[0]<250 and head[0]>-250 and
           head[1]<250 and head[1]>-250)

def change_direction(x,y):
    aim [0] = x
    aim [1] =y

def square(x,y,size,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

def snake_move() :
    global points
    head = copy.deepcopy(snakes[-1])
    head = [head[0]+aim[0],head[1]+aim[1]]
    if head in snakes or not inside(head) or head in barriers:
        for body in snakes:
            square(body[0], body[1], 10, 'black')
        messagebox.showinfo('game over!', "scores=" +str(points))
        return

    if head == food:
        while True:
            food[0] = randrange(-20, 20) * 10
            food[1] = randrange(-20, 20) * 10
            if food not in snakes and food not in barriers:
                break
        points = points + 1
        print (points)

        while True:
            if barriers:
                del barriers[0]
            else:
                break

        while True:
            new_barrier[0] = randrange(-24, 24) * 10
            new_barrier[1] = randrange(-24, 24) * 10
            if len(barriers) >= points:
                break
            if  new_barrier not in snakes:
                deep = copy.deepcopy(new_barrier)
                barriers.append(deep)
            print(barriers)

    else:
        snakes.pop(0)
    snakes.append (head)

    turtle.clear()
    for body in snakes:
        square(body[0], body[1], 10, 'green')
    square(food[0], food[1], 10, 'red')
    for barrier in barriers:
        square(barrier[0], barrier[1], 10, 'black')
    turtle.update()
    turtle.ontimer(snake_move,180)
    #时间间隔


# if __name__ == "__main__":
#     turtle.setup(500,500)
#
#     turtle.tracer(0)
#     turtle.hideturtle()
#     turtle.listen()
#     turtle.onkey(lambda: change_direction(0,10),"Up")
#     turtle.onkey(lambda: change_direction(0,-10),"Down")
#     turtle.onkey(lambda: change_direction(-10,0),"Left")
#     turtle.onkey(lambda: change_direction(10,0),"Right")
#
#
#     snake_move()
#     turtle.done()







