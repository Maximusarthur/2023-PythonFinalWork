import turtle as t
def draw4LevClover():
    t.title("四叶草")
    t.speed(6)
    t.screensize(800, 800)
    t.pensize(1)
    t.color('green')
    t.begin_fill()
    # 第一片叶子
    t.setheading(90)
    t.forward(5)
    t.setheading(60)
    t.circle(60, 20)
    t.circle(12, 180)
    t.setheading(140)
    t.circle(12, 180)
    t.circle(60, 25)
    t.setheading(110)
    t.forward(-4)
    # 第二片叶子
    t.setheading(170)
    t.forward(5)
    t.setheading(150)
    t.circle(60, 20)
    t.circle(12, 180)
    t.setheading(230)
    t.circle(12, 180)
    t.circle(60, 26)
    t.setheading(200)
    t.forward(-5)
    # 画杆
    t.setheading(250)
    t.circle(-120, 45)
    t.setheading(-70)
    t.forward(6)
    t.setheading(29)
    t.circle(140, 40)
    # 画第三片叶子
    t.setheading(270)
    t.forward(5)
    t.setheading(240)
    t.circle(60, 20)
    t.circle(12, 180)
    t.setheading(320)
    t.circle(12, 180)
    t.circle(60, 26)
    t.setheading(290)
    t.forward(-4)
    # 第四片叶子
    t.setheading(5)
    t.forward(5)
    t.setheading(330)
    t.circle(60, 20)
    t.circle(12, 180)
    t.setheading(40)
    t.circle(13, 180)
    t.left(5)
    t.circle(53, 35)
    t.setheading(20)
    t.forward(-5)
    t.end_fill()
    t.done()

draw4LevClover()