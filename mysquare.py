import turtle
import math


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(length)
    turtle.mainloop()


def polygon(t, length, n):
    angle = 360/n
    polyline(t, n, length, angle)


def circle(t, r):
    arc(t, r, 360)


def arc(t, r, angle):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length / 3) + 1
    step_length = arc_length/n
    step_angle = angle/n

    polyline(t, n, step_length, step_angle)


def polyline(t, n, length, angle):
    """Draws a line segment with the given length and
    angle (in degrees) between them. t is a turtle.
    """

    for i in range(n):
        t.fd(length)
        t.lt(angle)
    # turtle.mainloop()
