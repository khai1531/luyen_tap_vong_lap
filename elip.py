import cmath
import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
a = 100
b = 50
x = 0
y = 0
t.penup()
t.goto(x - a, y)
t.pendown()
for i in range(361):
    z = complex(a * cmath.cos(i * cmath.pi / 180), b * cmath.sin(i * cmath.pi / 180))
    x1 = z.real
    y1 = z.imag
    t.goto(x + x1, y + y1)
turtle.done()
