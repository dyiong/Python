"""
抽奖小工具
"""
from tkinter import *
from tkinter import Tk
import random

version = 1.0
isScroll = False
# 读取数据
with open("data.txt", "r") as file:
    dataLines = file.readlines()
dataLines = [x.strip("\n") for x in dataLines]


# 定时器
def run_counter():
    def counter():
        global dataLines, isScroll
        if isScroll:
            valueVar.set(random.choice(dataLines))
            root.after(100, counter)
        else:
            luckydata = valueVar.get()
            # print(luckydata)
            s = "中奖结果:\n" if not resultVar.get() else resultVar.get()
            resultVar.set(s + ' ' + luckydata)
            dataLines.remove(luckydata)
            # print(dataLines)
    counter()


def doClick():
    global isScroll
    isScroll = not isScroll
    if isScroll and len(dataLines):
        buttonText = "停止" if isScroll else "开始"
        doButton.config(text=buttonText)
        run_counter()


root = Tk()
root.title("抽奖小工具 v{}".format(version))
# 窗体
root_width = root.winfo_screenwidth() * 0.6
root_height = root.winfo_screenheight() * 0.7
ww = (root.winfo_screenwidth() - root_width) / 2
wh = (root.winfo_screenheight() - root_height) / 2
root.geometry("%dx%d+%d+%d" % (root_width, root_height, ww, wh))
# 随机值
valueVar = StringVar()
valueVar.set("无数据")
valueLabel = Label(root, textvariable=valueVar, font="微软雅黑 48 normal")
valueLabel.pack(pady=30)
# 结果
resultVar = StringVar()
resultLabel = Label(root, textvariable=resultVar, font="微软雅黑 15 normal", wraplength=root_width)
resultLabel.pack(side=BOTTOM, pady=30)
# 按钮
doButton = Button(root, text="开始", font="微软雅黑 14 normal", width=30, height=3, cursor="hand2", command=doClick)
doButton.pack(side=BOTTOM, pady=30)
root.mainloop()
