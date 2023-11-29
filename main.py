import os
import tkinter as tk
from tkinter import ttk


def run_python_file(file_name):
    # 运行指定的Python文件
    file_path = file_name
    if os.path.exists(file_path):
        os.system(f"python {file_path}")
    else:
        print(f"文件 '{file_path}' 不存在。")


def create_category_window(category_name, choices):
    # 创建类别窗口的方法
    second_window = tk.Toplevel(root)
    second_window.title(category_name)
    second_window.geometry("330x100")
    for i, (choice, file_name) in enumerate(choices):
        button = ttk.Button(second_window, text=choice, command=lambda fn=file_name: run_python_file(fn))
        button.grid(row=i // 2, column=i % 2, padx=5, pady=5)


def create_flower_window():
    # 创建花类界面的方法
    choices = [
        ("雪  花", "雪花.py"),
        ("荷  花", "荷花.py"),
        ("向日葵", "向日葵.py"),
        ("樱  花", "樱花.py")
    ]
    create_category_window("花类", choices)


def create_animal_window():
    # 创建动物类界面的方法
    choices = [
        ("人  脸", "人脸.py"),
        ("熊  猫", "熊猫.py"),
        ("蜗  牛", "蜗牛.py"),
        ("海  龟", "海龟.py")
    ]
    create_category_window("动物类", choices)


def create_cartoon_window():
    # 创建漫画人物类界面的方法
    choices = [
        ("大  白", "大白.py"),
        ("卡通鸡", "卡通鸡.py"),
        ("小猪佩奇", "小猪佩奇.py"),
        ("星之卡比", "星之卡比.py")
    ]
    create_category_window("漫画人物类", choices)


def create_green_window():
    # 创建植物类界面的方法
    choices = [
        ("一株草", "一株草.py"),
        ("四叶草", "四叶草.py"),
        ("圣诞树", "圣诞树.py"),
        ("樱  树", "樱花树.py")
    ]
    create_category_window("绿色植物类", choices)


def create_icon_window():
    # 创建图标类界面的方法
    choices = [
        ("太极图", "太极图.py"),
        ("勇士队队标", "勇士队队标.py"),
        ("时  钟", "时钟.py"),
        ("美队盾牌", "美队盾牌.py")
    ]
    create_category_window("图标类", choices)


def create_furniture_window():
    # 创建家具类界面的方法
    choices = [
        ("书  桌", "书桌.py"),
        ("凳  子", "凳子.py"),
        ("风  扇", "风扇.py"),
        ("电视机", "电视机.py")
    ]
    create_category_window("家具类", choices)


# 创建主界面
root = tk.Tk()
root.title("海龟简笔画")
root.geometry("500x450")  # 设置新的窗口尺寸
root.configure(bg="#f0f0f0")

# 加载图片并缩小
image = tk.PhotoImage(file="0.png")
image = image.subsample(2)  # 缩小为原来的一半

# 创建六个选择按钮
choices = [
    ("动物类", create_animal_window),
    ("花  类", create_flower_window),
    ("漫画人物类", create_cartoon_window),
    ("绿色植物类", create_green_window),
    ("图标类", create_icon_window),
    ("家具类", create_furniture_window)
]

row = 0
col = 0

for i, (choice, command) in enumerate(choices):
    button = ttk.Button(root, text=choice, command=command)
    button.grid(row=row+1, column=col, padx=5, pady=5)
    col += 1
    if col > 2:
        col = 0
        row += 1

# 添加图片
image_label = tk.Label(root, image=image)
image_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# 设置固定按钮大小
button_width = 20  # 设置固定的按钮宽度
button_height = 43  # 设置固定的按钮高度

style = ttk.Style()
style.configure("TButton", font=("Helvetica", int(button_height/4)))

for widget in root.winfo_children():
    if isinstance(widget, ttk.Button):
        style.configure(widget.winfo_class(), width=button_width, height=button_height)

# 运行主事件循环
root.mainloop()
