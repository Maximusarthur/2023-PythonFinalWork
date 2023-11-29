import turtle as t
pen = t.Turtle()  # 定义画笔实例
pen.speed(0)
pen.pensize(5)
pen.pu()
pen.right(90)# 头部
pen.goto(-100,200)
pen.pd()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.2
        pen.lt(3)  # 向左转3度
        pen.fd(a)  # 向前走a的步长
    else:
        a = a - 0.2
        pen.lt(3)
        pen.fd(a)
pen.pu()
pen.goto(-50,200)
pen.dot(20)
pen.goto(35,200)
pen.dot(20)
pen.right(90)
pen.pd()
# 身体
pen.pensize(5)
pen.fd(85)
pen.pu()
pen.goto(-70,150)
pen.pd()
pen.left(30)
pen.circle(200,90)
pen.pu()
pen.goto(50,150)
pen.left(30)
pen.pd()
pen.circle(-200,90)
pen.pu()
pen.goto(-140,-125)
pen.pd()
pen.left(90)
pen.circle(270,59)
#腿
pen.pu()
pen.goto(-120,-140)#左腿
pen.right(135)
pen.pd()
pen.circle(90,120)
pen.seth(-270)
pen.fd(90)
pen.pu()#右腿
pen.goto(100,-140)
pen.right(165)
pen.pd()
pen.circle(-90,120)
pen.seth(-270)
pen.fd(88)
#胳膊
pen.pu()#左臂
pen.goto(-130,100)
pen.pd()
pen.seth(200)
pen.circle(200,70)
pen.circle(30,180)
pen.fd(50)
pen.right(45)
pen.fd(50)
pen.up()#右臂
pen.goto(110,100)
pen.pd()
pen.seth(162)
pen.circle(200,-70)
pen.circle(30,-180)
pen.fd(-50)
pen.left(225)
pen.fd(50)
pen.hideturtle()
t.exitonclick()
