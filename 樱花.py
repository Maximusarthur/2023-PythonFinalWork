import turtle as t

toplevel = 8  # 树的层级
angle = 30  # 左枝的转角度数
rangle = 15  # 右枝的转角度数

# 绘制树的函数
def drawTree(length, level):
    t.left(angle)  # 绘制左枝
    t.color("black")
    t.forward(length)

    if level == toplevel:  # 如果达到最高层级，绘制叶子
        t.color("pink")
        t.circle(2, 360)

    if level < toplevel:  # 如果未达到最高层级，在左枝退回去之前递归绘制子树
        drawTree(length - 10, level + 1)
    t.back(length)

    t.right(angle + rangle)  # 绘制右枝
    t.color("black")
    t.forward(length)

    if level == toplevel:  # 如果达到最高层级，绘制叶子
        t.color("pink")
        t.circle(2, 360)

    if level < toplevel:  # 如果未达到最高层级，在右枝退回去之前递归绘制子树
        drawTree(length - 10, level + 1)
        t.color("black")
    t.back(length)
    t.left(rangle)

# 设置初始位置和速度
t.left(90)              # 设置初始朝向为向上
t.penup()               # 抬起画笔
t.back(300)             # 向后移动300个单位
t.pendown()             # 放下画笔
t.forward(100)          # 向前移动100个单位
t.speed('fastest')      # 设置绘制速度为最快

# 调用绘制树的函数开始绘制
drawTree(80, 1)

t.done()
