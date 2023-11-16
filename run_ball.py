import turtle
from ball import Vector
from ball import Canvas


num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas = Canvas(Vector(turtle.screensize()[0], turtle.screensize()[1])
                     , num_balls, 0.05 * turtle.screensize()[0])
turtle.colormode(255)
while True:
    turtle.clear()
    for i in canvas.balls:
        i.draw()
        i.move()
        # ball.draw_circle(ball_color[i], ball_radius, xpos[i], ypos[i])
        # ball.move_circle(i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
