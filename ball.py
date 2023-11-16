import turtle
import random


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


class Canvas:
    def __init__(self, canvas_size: Vector, ball_number, ball_radius):
        self.canvas_size = canvas_size
        self.ball_num = ball_number
        self.ball_radius = ball_radius
        self.balls = []
        for i in range(self.ball_num):
            ball_loc = Vector(random.randint(-1 * canvas_size.x + ball_radius, canvas_size.x - ball_radius),
                              random.randint(-1 * canvas_size.y + ball_radius, canvas_size.y - ball_radius))
            init_speed = Vector(random.randint(1, 0.01*canvas_size.x), (random.randint(1, 0.01*canvas_size.y)))
            ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.balls.append(Ball(ball_color, ball_radius, ball_loc, init_speed, self))

    def update(self):
        for i in self.balls:
            i.draw()
            i.move()



class Ball():
    def __init__(self, color, size, location: Vector, speed: Vector,canvas: Canvas):
        self.color = color
        self.size = size
        self.location = location
        self.speed = speed
        self.canvas_size = canvas.canvas_size

    def draw(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.location.x, self.location.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move(self):
        # update ball location by speed
        self.location += self.speed

        # reverse x speed when hit side wall
        if abs(self.location.x + self.speed.x) > (self.canvas_size.x - self.size):
            self.speed.x = -self.speed.x

        # reverse y speed when hit ceiling or floor
        if abs(self.location.y + self.speed.y) > (self.canvas_size.x - self.size):
            self.speed.y = -self.speed.y
