import turtle as t

t.speed(10)             # 设置绘制速度为10
t.screensize(bg='black')   # 设置背景颜色为黑色

for i in range(8):      # 循环8次绘制外部的八个三角形
    t.pensize(3)        # 设置画笔粗细为3
    t.pencolor('white')  # 设置画笔颜色为白色
    t.left(105-45*i)  # 左转一定角度
    t.forward(100)  # 向前移动100的距离
    t.right(30)  # 右转30度
    t.forward(100)  # 向前移动100的距离
    t.right(150)  # 右转150度
    t.forward(100)  # 向前移动100的距离
    t.right(30)  # 右转30度
    t.forward(100)  # 向前移动100的距离
    t.left(105)  # 左转105度

for j in range(8):  # 循环8次绘制内部的八个小三角形
    t.pencolor('white')  # 设置画笔颜色为白色
    t.pensize(3)  # 设置画笔粗细为3
    t.left(90-45*i)  # 左转一定角度
    t.begin_fill()  # 开始填充颜色
    t.pencolor('white')  # 设置画笔颜色为白色
    t.color('white')  # 设置填充颜色为白色
    t.left(15)  # 左转15度
    t.forward(30)  # 向前移动30的距离
    t.right(30)  # 右转30度
    t.forward(30)  # 向前移动30的距离
    t.right(150)  # 右转150度
    t.forward(30)  # 向前移动30的距离
    t.right(30)  # 右转30度
    t.forward(30)  # 向前移动30的距离
    t.left(105)  # 左转105度
    t.goto(0,0)  # 回到起始位置
    t.end_fill()  # 结束填充

t.hideturtle()  # 隐藏海龟形状
t.done()  # 完成绘制
