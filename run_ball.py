import turtle
from ball import Vector
from ball import Canvas


num_balls = int(input("Number of balls to simulate: "))
canvas = Canvas(Vector(turtle.screensize()[0], turtle.screensize()[1])
                , num_balls, 0.05 * turtle.screensize()[0])
while True:
    canvas.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
