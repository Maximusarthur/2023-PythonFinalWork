import turtle

def draw_head():
    # 初始化海龟模块
    turtle.setup(800, 600)  # 设置窗口大小
    window = turtle.Screen()
    window.title("Turtle Face")

    # 创建一个海龟实例
    pen = turtle.Turtle()
    pen.pensize(3)

    # 绘制脸轮廓
    pen.penup()
    pen.goto(0, -200)  # 将海龟移动到起始位置
    pen.pendown()
    pen.begin_fill()  # 开始填充脸的颜色
    pen.fillcolor("yellow")  # 设置脸的颜色
    pen.circle(200)  # 绘制半径为200的圆形
    pen.end_fill()  # 结束填充脸的颜色

    # 绘制眼睛
    pen.penup()
    pen.goto(-80, 50)  # 移动到左眼的位置
    pen.pendown()
    pen.begin_fill()  # 开始填充眼睛的颜色
    pen.fillcolor("white")  # 设置眼睛的颜色
    pen.circle(45)  # 绘制半径为50的眼睛
    pen.end_fill()  # 结束填充眼睛的颜色

    pen.penup()
    pen.goto(80, 50)  # 移动到右眼的位置
    pen.pendown()
    pen.begin_fill()  # 开始填充眼睛的颜色
    pen.fillcolor("white")  # 设置眼睛的颜色
    pen.circle(45)  # 绘制半径为50的眼睛
    pen.end_fill()  # 结束填充眼睛的颜色

    # 绘制眼珠
    pen.penup()
    pen.goto(-90, 70)  # 移动到左眼珠的位置
    pen.pendown()
    pen.begin_fill()  # 开始填充眼珠的颜色
    pen.fillcolor("black")  # 设置眼珠的颜色
    pen.circle(20)  # 绘制半径为20的眼珠
    pen.end_fill()  # 结束填充眼珠的颜色

    pen.penup()
    pen.goto(65, 70)  # 移动到右眼珠的位置
    pen.pendown()
    pen.begin_fill()  # 开始填充眼珠的颜色
    pen.fillcolor("black")  # 设置眼珠的颜色
    pen.circle(20)  # 绘制半径为20的眼珠
    pen.end_fill()  # 结束填充眼珠的颜色

    # 绘制鼻子
    pen.penup()
    pen.goto(-30, -15)  # 移动到鼻子的位置
    pen.pendown()
    pen.setheading(0)  # 设置海龟的朝向角度
    pen.width(3)  # 设置鼻子的线条宽度
    pen.fillcolor("red")  # 设置鼻子的颜色
    pen.begin_fill()  # 开始填充鼻子的颜色
    pen.circle(30, 120)  # 绘制半径为30的扇形
    pen.setheading(-120)  # 设置海龟的朝向角度
    pen.circle(30, 120)  # 绘制半径为30的扇形
    pen.end_fill()  # 结束填充鼻子的颜色

    # 绘制嘴巴
    pen.penup()
    pen.goto(-80, -80)  # 移动到嘴巴的起始位置
    pen.pendown()
    pen.setheading(-90)  # 设置海龟的朝向角度
    pen.width(6)  # 设置嘴巴的线条宽度
    pen.fillcolor("red")  # 设置嘴巴的颜色
    pen.begin_fill()  # 开始填充嘴巴的颜色
    pen.circle(80, 180)  # 绘制半径为100的半圆形
    pen.left(90)  # 左转90度
    pen.forward(160)  # 绘制嘴巴的长度
    pen.end_fill()  # 结束填充嘴巴的颜色

    # 绘制腮红
    pen.penup()
    pen.goto(-120, 30)  # 移动到左腮红的位置
    pen.pendown()
    pen.setheading(150)  # 设置海龟的朝向角度
    pen.width(3)  # 设置腮红的线条宽度
    pen.fillcolor("pink")  # 设置腮红的颜色
    pen.begin_fill()  # 开始填充腮红的颜色
    pen.circle(40, 240)  # 绘制半径为40的扇形
    pen.end_fill()  # 结束填充腮红的颜色

    pen.penup()
    pen.goto(120, -34)  # 移动到右腮红的位置
    pen.pendown()
    pen.setheading(-30)  # 设置海龟的朝向角度
    pen.width(3)  # 设置腮红的线条宽度
    pen.fillcolor("pink")  # 设置腮红的颜色
    pen.begin_fill()  # 开始填充腮红的颜色
    pen.circle(40, 240)  # 绘制半径为40的扇形
    pen.end_fill()  # 结束填充腮红的颜色

    # 关闭窗口
    window.mainloop()

# 调用函数绘制人脸
draw_head()









