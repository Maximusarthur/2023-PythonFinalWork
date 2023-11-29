import turtle
import time


def drawEllipse(a, b):
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + b
        else:
            a = a - b
        turtle.rt(3)
        turtle.fd(a)


# head
turtle.setup(800, 800, 0, 0)
turtle.pensize(5)
turtle.hideturtle()
turtle.speed(10)
turtle.color("#F49CA8")
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

# left eyes
turtle.penup()
turtle.goto(-60, 350)
turtle.pendown()
turtle.pencolor("#050306")
turtle.fillcolor("#474586")
turtle.begin_fill()
drawEllipse(0.4, 0.18)
turtle.end_fill()

turtle.fillcolor("#050306")
turtle.begin_fill()
drawEllipse(0.5, 0.12)
turtle.end_fill()

turtle.fillcolor("#F3EEEB")
turtle.begin_fill()
drawEllipse(0.5, 0.09)
turtle.end_fill()

# right eyes
turtle.penup()
turtle.goto(60, 350)
turtle.pendown()
turtle.fillcolor("#474586")
turtle.begin_fill()
drawEllipse(0.4, 0.18)
turtle.end_fill()

turtle.fillcolor("#050306")
turtle.begin_fill()
drawEllipse(0.5, 0.12)
turtle.end_fill()

turtle.fillcolor("#F3EEEB")
turtle.begin_fill()
drawEllipse(0.5, 0.09)
turtle.end_fill()

# left
turtle.penup()
turtle.goto(-150, 180)
turtle.pendown()
turtle.color("#E56B80")
turtle.begin_fill()
turtle.lt(90)
drawEllipse(0.3, 0.06)
turtle.end_fill()

# right
turtle.penup()
turtle.goto(100, 180)
turtle.pendown()
turtle.color("#E56B80")
turtle.begin_fill()
drawEllipse(0.3, 0.06)
turtle.end_fill()

# left hand
turtle.penup()
turtle.goto(-160, 180)
turtle.pendown()
turtle.color("#F49CA8")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# right hand
turtle.penup()
turtle.goto(260, 185)
turtle.pendown()
turtle.color("#F49CA8")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
time.sleep(1)

# left foot
turtle.penup()
turtle.goto(-120, 50)
turtle.pendown()
turtle.color("#9B384D")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# right foot
turtle.penup()
turtle.goto(130, 40)
turtle.pendown()
turtle.color("#9B384D")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
time.sleep(1)

# mouse#562B25 #F38D77
turtle.pensize(1)
turtle.penup()
turtle.goto(-20, 180)
turtle.pendown()
turtle.color("#562B25")
turtle.begin_fill()
turtle.seth(-90)
turtle.circle(25, 180)
turtle.end_fill()

time.sleep(5)

turtle.done()
