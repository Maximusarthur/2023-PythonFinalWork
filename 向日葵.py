import turtle

# 创建海龟对象
t = turtle.Turtle()
m = turtle.Turtle()

# 设置画笔颜色和填充颜色
t.color('black', 'yellow')
m.color('red')

# 定义绘制花瓣的函数
def draw_huban(heading_angle, l, angle):
    t.setheading(heading_angle)  # 设置海龟的朝向角度
    t.right(angle / 2)  # 右转一半的角度
    t.begin_fill()  # 开始填充
    t.forward(l)  # 向前移动长度l
    t.left(angle)  # 左转给定的角度
    t.forward(l)  # 向前移动长度l
    t.left(180 - angle)  # 左转180减去给定的角度
    t.forward(l)  # 向前移动长度l
    t.left(angle)  # 左转给定的角度
    t.end_fill()  # 结束填充
    turtle.tracer(True)  # 显示绘制过程

R = 100  # 花朵半径

# 将m海龟定位到起始点
m.penup()
m.goto(0, 0)
m.setheading(270)  # 设置朝向向下
m.forward(R)  # 向前移动半径的长度
m.setheading(0)  # 设置朝向向右
m.pendown()

t.speed(30)  # 设置绘制速度为30
stepangle = 20  # 每次绘制的角度

# 绘制花瓣
for i in range(int(360 / stepangle)):
    m.circle(R, stepangle)  # 绘制圆弧
    m_dire = m.heading()  # 获取当前朝向角度
    m_posi = m.pos()  # 获取当前位置坐标
    t.penup()
    t.goto(m_posi)
    t.pendown()
    draw_huban(m_dire - 90, R, 30)  # 绘制花瓣

# 间隔绘制花瓣
m.circle(R, stepangle / 2)
for i in range(int(360 / stepangle)):
    m.circle(R, stepangle)
    m_dire = m.heading()
    m_posi = m.pos()
    t.penup()
    t.goto(m_posi)
    t.pendown()
    draw_huban(m_dire - 90, R, 30)  # 绘制花瓣

# 绘制实心部分
offset = R
m.penup()
m.goto(0, -R - offset)
m.pendown()
m.color('orange')
m.setheading(0)
m.begin_fill()
m.circle(R + offset)
m.end_fill()

# 隐藏海龟对象
m.hideturtle()
t.hideturtle()

# 完成绘制
turtle.done()
