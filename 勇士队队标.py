import turtle as t
def drawTeamLogo():
    t.speed(5)
    t.screensize(600, 600, "yellow")  # 设置画布的宽、高均为600，背景颜色为黄色

    # 圆：蓝-黄-蓝
    t.pensize(5)
    for x in range(1, 4):
        if x % 2 == 1:
            t.pencolor('blue')
            t.fillcolor('blue')
        else:
            t.pencolor('yellow')
            t.fillcolor('yellow')
        t.begin_fill()
        t.up()
        if x == 1:
            t.goto(0, -250)
            t.down()
            t.circle(250)
        elif x == 2:
            t.goto(0, -233)
            t.down()
            t.circle(233)
        else:
            t.goto(0, -220)
            t.down()
            t.circle(220)
        t.end_fill()

    # 大桥横线下一
    t.up()
    t.goto(-203, -102)
    t.down()
    t.pencolor('yellow')
    t.pensize(15)
    t.rt(2)
    t.fd(400)

    # 大桥横线上二
    t.up()
    t.goto(-205, -90)
    t.down()
    t.lt(3)
    t.fd(415)
    t.up()
    t.goto(-205, -93)
    t.down()
    t.rt(0.5)
    t.fd(410)

    # 大桥竖线左二
    t.pensize(5)
    t.up()
    t.goto(-120, -195)
    t.down()
    t.fillcolor('yellow')
    t.begin_fill()
    t.rt(0.5)
    t.lt(90)
    t.fd(303)
    t.rt(80)
    t.fd(13)
    t.lt(80)
    t.bk(313)
    t.end_fill()

    t.up()
    t.goto(-130, -187)
    t.down()
    t.begin_fill()
    t.rt(1)
    t.fd(283)
    t.rt(79)
    t.fd(13)
    t.lt(80)
    t.bk(298)
    t.end_fill()

    # 大桥竖线右一下
    t.up()
    t.goto(-92, -208)
    t.down()
    t.pensize(5)
    t.fillcolor('yellow')
    t.begin_fill()
    t.fd(80)
    t.rt(90)
    t.fd(20)
    t.rt(83)
    t.fd(90)
    t.lt(173)
    t.goto(-92, -208)
    t.end_fill()

    # 大桥竖线右一上
    t.pensize(5)
    t.up()
    t.goto(-92, -90)
    t.down()
    t.begin_fill()
    t.fd(198)
    t.rt(100)
    t.fd(15)
    t.rt(79.7)
    t.fd(200)
    t.rt(90.3)
    t.fd(17)
    t.end_fill()

    # 大桥竖线中间横线(6条)
    t.pensize(21)
    t.up()
    t.goto(-110, 90)
    t.down()
    t.rt(180)
    t.fd(20)

    t.pensize(10)
    t.up()
    t.goto(-110, 66)
    t.down()
    t.fd(20)

    t.up()
    t.goto(-110, 44)
    t.down()
    t.fd(20)

    t.up()
    t.goto(-110, 22)
    t.down()
    t.fd(20)

    t.up()
    t.goto(-110, -7)
    t.down()
    t.fd(20)

    t.up()
    t.goto(-110, -36)
    t.down()
    t.fd(20)

    # 左侧弧线
    t.pensize(10)
    t.up()
    t.goto(-228, -8)
    t.down()
    t.lt(27)
    t.circle(300, 27)
    t.circle(300, -27)
    t.rt(27)

    # 右侧弧线
    t.up()
    t.goto(215, -70)
    t.down()
    t.rt(8)
    t.circle(480, -42)
    t.circle(480, 42)
    t.lt(8)

    # 左侧斜线(3条)
    t.pensize(7)
    t.up()
    t.goto(-125, 75)
    t.down()
    t.rt(116)
    t.fd(174)
    t.up()
    t.goto(-185, 20)
    t.down()
    t.fd(88)
    t.up()
    t.goto(-125, 0)
    t.down()
    t.fd(95)
    t.lt(116)

    # 右侧斜线(9条)
    t.up()
    t.goto(65, -80)
    t.down()
    t.lt(110)
    t.fd(75)
    t.up()
    t.goto(-43, -83)
    t.down()
    t.fd(93)

    t.up()
    t.goto(-16, -83)
    t.down()
    t.fd(170)

    t.up()
    t.goto(11, -83)
    t.down()
    t.fd(140)

    t.up()
    t.goto(38, -83)
    t.down()
    t.fd(100)

    t.up()
    t.goto(92, -83)
    t.down()
    t.fd(60)

    t.up()
    t.goto(119, -83)
    t.down()
    t.fd(47)

    t.up()
    t.goto(146, -83)
    t.down()
    t.fd(30)

    t.up()
    t.goto(173, -83)
    t.down()
    t.fd(20)


    t.done()

drawTeamLogo()
