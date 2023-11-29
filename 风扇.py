import turtle

def draw_fan():
    # 创建一个海龟对象，用于绘制
    t = turtle.Turtle()

    # 设置绘制速度和粗细
    t.speed(10)
    t.pensize(3)

    # 绘制底座
    t.penup()
    t.goto(-40, 10)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.setheading(-115)
    t.forward(120)
    t.setheading(0)
    t.forward(180)
    t.setheading(115)
    t.forward(120)
    t.end_fill()
    t.penup()
    t.backward(120)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.setheading(0)
    t.forward(30)
    t.setheading(-90)
    t.forward(20)
    t.setheading(180)
    t.forward(240)
    t.setheading(90)
    t.forward(20)
    t.setheading(0)
    t.forward(240)
    t.end_fill()

    # 绘制风扇中心
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.setheading(0)
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(0, 20)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    t.penup()
    t.goto(40, 90)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    t.penup()
    t.goto(-40, 90)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    t.penup()
    t.goto(0, 70)
    t.pendown()
    t.fillcolor("tan")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    # 绘制按钮
    t.penup()
    t.goto(-15, -20)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.setheading(0)
    t.forward(30)
    t.setheading(-90)
    t.forward(10)
    t.setheading(180)
    t.forward(30)
    t.setheading(90)
    t.forward(10)
    t.end_fill()

    t.penup()
    t.goto(-40, -70)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.penup()
    t.goto(60, -70)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()





    # 显示绘画结果
    turtle.done()

draw_fan()