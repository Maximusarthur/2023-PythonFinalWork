import turtle

def draw_panda():
    # 创建一个海龟实例
    pen = turtle.Turtle()

    # 绘制熊猫的头部
    pen.fillcolor("white")  # 设置填充颜色为白色
    pen.width(3)
    pen.begin_fill()  # 开始填充
    pen.circle(100)  # 绘制半径为100的圆形作为头部
    pen.end_fill()  # 结束填充

    # 绘制熊猫的耳朵
    pen.penup()
    pen.goto(-50, 185)  # 移动到左耳朵位置
    pen.pendown()
    pen.fillcolor("black")  # 设置填充颜色为黑色
    pen.begin_fill()  # 开始填充
    pen.setheading(105)  # 设置海龟的朝向角度
    pen.circle(30, 240)  # 绘制耳朵
    pen.end_fill()  # 结束填充

    pen.penup()
    pen.goto(85, 152)  # 移动到右耳朵位置
    pen.pendown()
    pen.fillcolor("black")  # 设置填充颜色为黑色
    pen.begin_fill()  # 开始填充
    pen.setheading(17)  # 设置海龟的朝向角度
    pen.circle(30, 240)  # 绘制半径为30的圆弧作为耳朵
    pen.end_fill()  # 结束填充

    # 绘制熊猫的眼睛
    pen.penup()
    pen.goto(-60, 130)  # 移动到左眼位置
    pen.pendown()
    pen.fillcolor("black")  # 设置填充颜色为黑色
    pen.begin_fill()  # 开始填充
    pen.circle(20)  # 绘制半径为20的圆形作为眼睛
    pen.end_fill()  # 结束填充

    pen.penup()
    pen.goto(27, 130)  # 移动到右眼位置
    pen.pendown()
    pen.fillcolor("black")  # 设置填充颜色为黑色
    pen.begin_fill()  # 开始填充
    pen.circle(20)  # 绘制半径为20的圆形作为眼睛
    pen.end_fill()  # 结束填充

    # 绘制熊猫眼白
    pen.penup()
    pen.goto(-55, 130)  # 移动到左眼白位置
    pen.pendown()
    pen.fillcolor("white")  # 设置填充颜色为白色
    pen.begin_fill()  # 开始填充
    pen.circle(10)  # 绘制半径为20的圆形作为眼睛
    pen.end_fill()  # 结束填充

    pen.penup()
    pen.goto(33, 130)  # 移动到右眼白位置
    pen.pendown()
    pen.fillcolor("white")  # 设置填充颜色为白色
    pen.begin_fill()  # 开始填充
    pen.circle(10)  # 绘制半径为20的圆形作为眼睛
    pen.end_fill()  # 结束填充

    # 绘制熊猫的鼻子
    pen.penup()
    pen.goto(-7, 85)  # 移动到鼻子位置
    pen.setheading(-60)  # 设置海龟朝向
    pen.width(3)  # 设置线条宽度
    pen.pendown()
    pen.fillcolor("black")  # 设置填充颜色为黑色
    pen.begin_fill()  # 开始填充
    pen.circle(10, 120)
    pen.setheading(120)
    pen.circle(10, 120)
    pen.end_fill()  # 结束填充

    # 绘制熊猫的嘴巴
    pen.penup()  # 起笔
    pen.goto(-25, 40)  # 移动到嘴巴起始位置
    pen.pendown()  # 落笔
    pen.setheading(-75)  # 设置海龟的朝向角度
    pen.width(3)  # 设置线条宽度为3
    pen.fillcolor("red")  # 设置填充颜色为粉红色
    pen.begin_fill()  # 开始填充
    pen.circle(30, 150)  # 绘制半径为30的扇形作为嘴巴
    pen.setheading(180)
    pen.forward(56)
    pen.end_fill()  # 结束填充

    # 绘制熊猫的腮红
    pen.penup()  # 起笔
    pen.goto(-70, 70)  # 海龟移动到左腮红的位置
    pen.setheading(-60)
    pen.fillcolor("pink")  # 设置填充颜色
    pen.pencolor("pink")  # 设置画笔颜色为粉色
    pen.pendown()  # 落笔
    pen.begin_fill()  # 开始填充
    pen.circle(20, 150)  # 绘制半径为20，圆心角为120度的圆弧
    pen.setheading(120)
    pen.circle(20, 150)  # 绘制半径为20，圆心角为120度的圆弧
    pen.end_fill()  # 结束填充

    pen.penup()  # 起笔
    pen.goto(45, 70)  # 海龟移动到右腮红的位置
    pen.setheading(-60)
    pen.fillcolor("pink")  # 设置填充颜色
    pen.pencolor("pink")  # 设置画笔颜色为粉色
    pen.pendown()  # 落笔
    pen.begin_fill()  # 开始填充
    pen.circle(20, 150)  # 绘制半径为20，圆心角为120度的圆弧
    pen.setheading(120)
    pen.circle(20, 150)  # 绘制半径为20，圆心角为120度的圆弧
    pen.end_fill()  # 结束填充

    # 绘制熊猫的身体
    pen.penup()
    pen.goto(-70, 26)  # 移动到身体起始位置
    pen.pendown()
    pen.pencolor("black")  # 设置线条颜色为黑色
    pen.setheading(-90)
    pen.forward(70)
    pen.circle(70, 180)  # 绘制半径为70的圆形作为身体
    pen.setheading(90)
    pen.forward(70)

    # 绘制熊猫的四肢
    pen.penup()
    pen.goto(-70, 26)  # 移动到左手位置
    pen.pendown()
    pen.setheading(-120)
    pen.fillcolor("black")
    pen.begin_fill()  # 开始填充
    pen.circle(60, 70)
    pen.setheading(-45)
    pen.circle(70, 45)
    pen.setheading(0)
    pen.circle(20, 180)
    pen.goto(-70, 26)
    pen.end_fill()

    pen.penup()
    pen.goto(27, -65)  # 移动到右手位置
    pen.pendown()
    pen.setheading(5)
    pen.fillcolor("black")
    pen.begin_fill()  # 开始填充
    pen.circle(60, 120)
    pen.penup()
    pen.goto(27, -25)
    pen.pendown()
    pen.setheading(180)
    pen.circle(20, 180)
    pen.goto(-70, 26)
    pen.end_fill()

    pen.penup()
    pen.goto(-60, -77)  # 移动到左脚位置
    pen.pendown()
    pen.setheading(-160)
    pen.fillcolor("black")
    pen.begin_fill()  # 开始填充
    pen.circle(30, 240)
    pen.end_fill()

    pen.penup()
    pen.goto(20, -113)  # 移动到右脚位置
    pen.pendown()
    pen.setheading(-80)
    pen.fillcolor("black")
    pen.begin_fill()  # 开始填充
    pen.circle(30, 240)
    pen.end_fill()

    # 隐藏海龟
    pen.hideturtle()

    # 关闭窗口
    turtle.done()

# 调用绘制熊猫的方法
draw_panda()
