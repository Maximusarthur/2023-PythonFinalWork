import turtle

def draw_tutle():
    # 创建一个海龟对象，用于绘制
    t = turtle.Turtle()

    # 设置绘制速度和粗细
    t.speed(10)
    t.pensize(3)
    
    # 绘制脑袋
    t.penup()
    t.goto(30, 152)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.setheading(55)
    t.circle(30, 240)
    t.end_fill()
    
    # 绘制眼睛
    t.penup()
    t.goto(-5, 185)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    
    t.penup()
    t.goto(10, 185)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    
    # 绘制四肢
    t.penup()
    t.goto(-50, 138)
    t.fillcolor("yellow")
    t.pendown()
    t.begin_fill()
    t.setheading(105)
    t.circle(20, 270)
    t.end_fill()
    
    t.penup()
    t.goto(70, 110)
    t.fillcolor("yellow")
    t.pendown()
    t.begin_fill()
    t.setheading(5)
    t.circle(20, 270)
    t.end_fill()
    
    t.penup()
    t.goto(-60, 50)
    t.fillcolor("yellow")
    t.pendown()
    t.begin_fill()
    t.setheading(170)
    t.circle(20, 270)
    t.end_fill()
    
    t.penup()
    t.goto(50, 20)
    t.fillcolor("yellow")
    t.pendown()
    t.begin_fill()
    t.setheading(-60)
    t.circle(20, 270)
    t.end_fill()

    # 绘制身体
    t.penup()
    t.goto(0, 0)
    t.fillcolor("green")
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.circle(80)
    t.end_fill()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(90)
    t.forward(40)
    
    t.setheading(150)
    t.forward(40)
    t.setheading(-150)
    t.forward(40)
    t.backward(40)
    
    
    t.setheading(90)
    t.forward(40)
    t.setheading(150)
    t.forward(40)
    t.backward(40)
    
    t.setheading(30)
    t.forward(40)
    t.setheading(90)
    t.forward(40)
    t.backward(40)
    
    t.setheading(-30)
    t.forward(40)
    t.setheading(30)
    t.forward(40)
    t.backward(40)
    
    t.setheading(-90)
    t.forward(40)
    t.setheading(-30)
    t.forward(40)
    t.backward(40)
    
    t.setheading(-150)
    t.forward(40)
    
    # 隐藏海龟
    t.hideturtle()

    # 关闭窗口
    turtle.done()
    
draw_tutle()