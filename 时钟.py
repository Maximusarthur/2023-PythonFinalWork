import turtle as t
import datetime
def skip(step):
    t.penup()
    t.forward(step)
    t.pendown()

def mkhand(name,length):
    # 注册表针形状
    t.reset()
    skip(-length*0.1)
    t.begin_poly()
    t.forward(length*1.1)
    t.end_poly()
    handform= t.get_poly()
    t.register_shape(name,handform)

def init():
    global sechand,minhand,hurhand,printer # 初始化四个全局变量（秒针，分针，时针，输出文字的turtle）
    t.mode("logo") # 标准模式,指针指向北方
    mkhand("sechand",125)
    mkhand("minhand",130)
    mkhand("hurhand",90)
    # 创建turtle对象
    sechand = t.Turtle()
    sechand.shape("sechand")
    minhand = t.Turtle()
    minhand.shape("minhand")
    hurhand = t.Turtle()
    hurhand.shape("hurhand")
    for hand in sechand,minhand,hurhand:
        hand.shapesize(1,1,3)
        hand.speed(0)
    # 建立一个输出文字的turtle
    printer = t.Turtle()
    printer.hideturtle()
    printer.penup()

def setupColock(radius):
    # 建立时钟的外框
    t.reset()
    t.pensize(7)
    for i in range(60):
        skip(radius)
        if i %5 == 0:
            t.forward(20)
            skip(-radius-20)
        else:
            t.dot(5)
            skip(-radius)
        t.right(6)

def week(tody):
    # 返回今天是星期几
    week=["星期一","星期二","星期三","星期三","星期四","星期五","星期六","星期日"]
    return week[tody.weekday()]

def date(tody):
    y = tody.year
    m = tody.month
    d = tody.day
    return "%s %d %d" %(y,m,d)

def tick():
    # 绘制时针的动态显示
    today = datetime.datetime.now()
    second = today.second+today.microsecond*0.000001
    minute = today.minute+second/60.0
    hour = today.hour+second/60.0
    sechand.setheading(6*second)
    minhand.setheading(6*minute)
    hurhand.setheading(30*hour)
    t.tracer(False)
    printer.forward(65)
    printer.write(week(today),align="center",font=("Courier",14,"bold"))
    printer.back(130)
    printer.write(date(today),align="center",font=("Courier",14,"bold"))
    printer.home()
    t.tracer(True)
    t.ontimer(tick(),100)
    # 100ms后再次调用tick函数

def drawClock():
    t.tracer(False)
    init()
    setupColock(160)
    tick()

while True:
    drawClock()






