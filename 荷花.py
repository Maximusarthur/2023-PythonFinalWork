import turtle as t

# 绘制花瓣的函数
def huaban():
    t.pensize(3)
    t.pencolor("pink")
    t.circle(100, 90)  # 绘制一个四分之一圆
    t.lt(90)  # 左转90度
    t.circle(100, 90)  # 绘制另一个四分之一圆
    t.lt(90)  # 左转90度

# 绘制花朵
for i in range(9):
    huaban()
    t.lt(15)  # 左转15度

t.speed(50)
t.pensize(9)
t.pencolor("green")
t.seth(270)  # 设置海龟的朝向为270度（向下）

# 绘制茎
for j in range(36):
    t.fd(5)  # 前进5个单位
    t.rt(1)  # 右转1度

t.exitonclick()  # 点击关闭海龟绘图窗口
