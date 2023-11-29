import turtle as tl
import random as rd
import math as mt

# 根据给定的参数n和t，在屏幕上画出一个数字为n的绿色箭头，并使箭头的粗细和颜色与数字n相关联。同时，箭头向右旋转一定角度，然后向前移动一定距离。
def write(n, t):
    print(n)
    tl.pensize(mt.sqrt(n + 1) / 10)
    tl.pencolor(0.3, 0.9, 0.3)
    tl.right(50 / (n + 1))
    tl.forward(n / 20)
    # 根据给定的参数n，在屏幕上画出一个由若干小线段组成的随机图案。每个小线段长度为10 * n / t，左转或右转的角度为15 * n / t，转向的方向由一个随机数决定。其中，n参数用于控制图案的大小和线条的粗细，t参数用于控制线条的长度。
    def pt(n):
        d = rd.randint(0, 1)
        if d:
            tl.left(15 * n / t)
            tl.forward(10 * n / t)
            tl.backward(10 * n / t)
            tl.right(15 * n / t)
        else:
            tl.right(15 * n / t)
            tl.forward(10 * n / t)
            tl.backward(10 * n / t)
            tl.left(15 * n / t)

    if n > 0:
        pt(n)
        write(n - 1, t)


def move(x, y):
    tl.penup()
    tl.goto(x, y)
    tl.pd()


def m(n, t, Ysize, angle):
    Y = Ysize
    tl.right(50 / (n + 1))
    tl.pensize(mt.sqrt(n) / 5)
    tl.pencolor(0.1, 0.7, 0.1)
    tl.forward(25 * n / t)
    if (n > 0):
        q1 = 45 * n / t
        q2 = 45 * n / t
        list = tl.position()
        x1 = list[0]
        y1 = list[1]
        angle = angle - 50 / (n + 1)
        tl.left(q1)
        write(Y * n, Y * n)
        move(x1, y1)
        tl.setheading(angle)
        tl.right(q2)
        write(Y * n, Y * n)
        move(x1, y1)
        tl.setheading(angle)
        # tl.right(180-45 * n / t)
        m(n - 1, t, Ysize, angle)


def drawGrass():
    tl.screensize(1000, 1000)
    tl.speed(0)
    tl.delay(0)
    tl.bgcolor(1, 1, 1) # 将背景颜色设置为白色
    tl.left(90)
    tl.penup()
    tl.backward(100)
    tl.pendown()
    m(20, 20, 4, 90)
    tl.hideturtle()
    tl.mainloop()


drawGrass()
