import turtle

def draw_snail():
    # 创建一个海龟对象，用于绘制
    t = turtle.Turtle()

    # 设置绘制速度和粗细
    t.speed(10)
    t.pensize(5)

    # 绘制身体
    t.penup()
    t.goto(30, -45)
    t.fillcolor("pink")
    t.begin_fill()
    t.pendown()
    t.setheading(180)
    t.circle(50, -75)
    t.setheading(-90)
    t.forward(15)
    t.setheading(177)
    t.forward(150)
    t.setheading(-30)
    t.circle(60, -60)
    t.setheading(-15)
    t.circle(30, -250)
    t.end_fill()

    # 开始填充外轮廓并绘制
    t.penup()
    t.goto(0, 0)
    t.fillcolor("brown")
    t.begin_fill()
    t.setheading(0)
    t.pendown()
    t.circle(20)
    t.penup()
    t.goto(0, -25)
    t.pendown()
    t.circle(45)
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.circle(70)
    t.end_fill()

    # 绘制眼睛
    t.penup()
    t.goto(-100, -10)
    t.fillcolor("black")
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    # 绘制嘴
    t.color("black")
    t.width(2)
    t.penup()
    t.goto(-120, -25)
    t.pendown()
    t.setheading(0)
    t.circle(30, 45)

    # 绘制触角
    t.width(5)
    t.penup()
    t.goto(-110, 20)
    t.setheading(105)
    t.pendown()
    t.forward(20)
    t.setheading(15)
    t.circle(10)

    t.penup()
    t.goto(-90, 20)
    t.setheading(85)
    t.pendown()
    t.forward(20)
    t.setheading(0)
    t.circle(10)


    # 隐藏海龟并显示绘画结果
    turtle.done()


draw_snail()
