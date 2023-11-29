import turtle

def draw_tv():
    # 创建一个海龟对象，用于绘制
    t = turtle.Turtle()

    # 设置绘制速度和粗细
    t.speed(10)
    t.pensize(3)

    # 绘制电视机的框架
    t.color("black")
    t.begin_fill()
    t.penup()
    t.goto(-100, -50)
    t.pendown()
    t.goto(100, -50)
    t.goto(100, 50)
    t.goto(-100, 50)
    t.goto(-100, -50)
    t.end_fill()

    # 绘制电视机的屏幕
    t.color("green")
    t.begin_fill()
    t.penup()
    t.goto(-90, -40)
    t.pendown()
    t.goto(90, -40)
    t.goto(90, 40)
    t.goto(-90, 40)
    t.goto(-90, -40)
    t.end_fill()

    # 绘制电视机上的花纹
    t.color("gray")
    t.penup()
    t.goto(-70, -30)
    t.pendown()
    t.goto(-50, -10)
    t.goto(50, -10)
    t.goto(70, -30)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.fillcolor("black")
    t.setheading(-90)
    t.forward(30)

    # 绘制底座
    t.penup()
    t.goto(-10, -50)
    t.pendown()
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    t.setheading(-90)
    t.forward(40)
    t.setheading(0)
    t.forward(20)
    t.setheading(90)
    t.forward(40)
    t.end_fill()

    t.penup()
    t.goto(-35, -90)
    t.pendown()
    t.begin_fill()
    t.setheading(-60)
    t.circle(40, 120)
    t.setheading(120)
    t.circle(40, 120)
    t.end_fill()

    # 显示绘画结果并隐藏海龟
    turtle.done()

draw_tv()