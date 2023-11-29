import turtle as t
def drawTaijitu():
    t.speed(5)
    t.screensize(600,600)
    t.penup()
    t.goto(0,-200)
    t.pendown()
    t.pensize(2)
    # 画出外轮廓
    t.circle(200)

    # 绘制阳鱼
    t.fillcolor("white")
    t.begin_fill()
    t.left(180)
    t.circle(-100,180)
    t.circle(100,180)
    t.end_fill()

    # 绘制阴鱼眼
    t.fillcolor("black")
    t.begin_fill()
    t.right(180)
    t.circle(-200, 180)
    t.circle(-100,180)
    t.circle(100,180)
    t.end_fill()

    # 绘制阳鱼眼
    t.penup()
    t.goto(0,75)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(-200/8)
    t.end_fill()

    # 绘制阴鱼眼
    t.penup()
    t.goto(0,-75)
    t.pendown()
    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    t.circle(200/8)
    t.end_fill()

    t.done()

drawTaijitu()