import turtle as t
import math
t.speed(5)
t.pensize(5)
#画一个美国队长盾牌
def drawSheild():
    #画红色圆
    t.penup()
    t.goto(0,-200)
    t.pendown()
    t.setup(500,500)
    t.fillcolor("red")
    t.begin_fill()
    t.circle(200)
    t.end_fill()

    #画银色圆
    t.penup()
    t.goto(0,-160)
    t.fillcolor("#C0C0C0")
    t.begin_fill()
    t.circle(160)
    t.end_fill()

    #画红色圆
    t.penup()
    t.goto(0,-120)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(120)
    t.end_fill()


    #画蓝色圆
    t.penup()
    t.goto(0,-80)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(80)
    t.end_fill()

    #画银色五角星
    t.penup()
    t.goto(0,80)
    t.right(72)
    t.pencolor("#C0C0C0")
    t.fillcolor("#C0C0C0")
    t.begin_fill()
    for i in range(5):
        t.forward(80*2*math.cos(18*math.pi/180))
        t.right(144)
    t.end_fill()

    t.done()
drawSheild()