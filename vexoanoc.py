import turtle

t = turtle.Turtle()
t.speed(0)

t.penup()
t.setpos(0, 0)
t.pendown()
t.setheading(90)

for i in range(100):
    t.forward(i)
    t.right(45)
turtle.done()