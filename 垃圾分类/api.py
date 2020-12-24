import base64
import requests
import json
from tkinter import *
from tkinter import filedialog


def base64_img(img_path):
    with open(img_path, 'rb') as img:
        # print(img.read())
        suffix = img_path.split('.')[-1]
        # print(suffix)
        img_base64 = str(base64.b64encode(img.read()), encoding='utf-8')
        # print('data:image/' + suffix + ';base64,' + img_base64)
        return 'data:image/' + suffix + ';base64,' + img_base64


def get_data(img_base64):
    url = "http://api.tianapi.com/txapi/imglajifenlei/"
    headers = {'content-type': "application/x-www-form-urlencoded"}
    data = {
        # 修改的地方
        "key": "<填写你的key>",
        "img": img_base64
    }
    response = requests.post(url, data=data, headers=headers)
    # print(json.loads(response.text))
    # print(type(json.loads(response.text)))
    laji_data = json.loads(response.text)

    return laji_data


def classification(num):
    if num == 0:
        return '可回收垃圾'
    if num == 1:
        return '有害垃圾'
    if num == 2:
        return '厨余垃圾'
    if num == 3:
        return '其他垃圾'
    else:
        return '无法识别'


img_path = '图片地址'


# print(open_img('test.jpg'))
def get_img_path():
    global img_path
    img_path = filedialog.askopenfilename()
    message_img_path['text'] = img_path
    # print(img_path)
    return img_path


def view():
    global img_path
    base64_img_data = base64_img(img_path)
    # print(base64_img_data)
    laji_data = get_data(base64_img_data)
    # print(laji_data)
    print(type(laji_data))
    newslist = laji_data['newslist']
    print(newslist)
    first_data = newslist[0]
    second_data = newslist[1]
    third_data = newslist[2]
    first_text['text'] = first_data['name'] + " 可信度: " + str(first_data['trust'])[0:4] + classification(first_data['lajitype'])
    second_text['text'] = second_data['name'] + " 可信度: " + str(second_data['trust'])[0:4] + classification(second_data['lajitype'])
    third_text['text'] = third_data['name'] + " 可信度: " + str(third_data['trust'])[0:4] + classification(third_data['lajitype'])


# 创建root界面
root = Tk()
root.title('垃圾分类图像识别')
root.geometry("600x400+400+300")
# file_path = filedialog.askopenfilename()
# print(file_path)

# 按钮
buttonFrame = Frame(root)
Button(buttonFrame, text='打开文件', command=get_img_path).pack(side=LEFT, padx=5, pady=5)
Button(buttonFrame, text='分析图片', command=view).pack(side=LEFT, padx=5, pady=5)
buttonFrame.pack()

# 显示
message_img_path = Label(root, text=img_path)
message_img_path.pack()

first_text = Label(root, text='')
first_text.pack()
second_text = Label(root, text='')
second_text.pack()
third_text = Label(root, text='')
third_text.pack()

root.mainloop()
