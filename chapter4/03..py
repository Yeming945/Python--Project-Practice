# translate_tet.py
from tkinter import Label, Tk, Entry, Button, StringVar
from urllib import request
from urllib import parse

import json
import hashlib


def translate_word(en_str):
    URL = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

    Form_Data = {}
    Form_Data['from'] = 'en'
    Form_Data['to'] = 'zh'
    Form_Data['q'] = en_str  # 要翻译的数据
    Form_Data['appid'] = '20181223000251282'  # 申请的app id
    Form_Data['salt'] = 'l435660288'
    Key = 'XtvL6yH23m_k7ZcPTW1j'  # 平台分配的密钥
    m = Form_Data['appid'] + en_str + Form_Data['salt'] + Key
    m_MD5 = hashlib.md5(m.encode('utf-8'))
    Form_Data['sign'] = m_MD5.hexdigest()

    data = parse.urlencode(Form_Data).encode(
        'utf-8')  # 使用 urlencode （）方法转换标准格式
    response = request.urlopen(URL, data)  # 传递 Request 对象和转换完格式的数据
    html = response.read().decode('utf-8')  # ＃读取信息并解码
    translate_results = json.loads(html)  # 使用 JSON
    print(translate_results)  # 打印出JSON数据
    # 找到翻译结果
    translate_results = translate_results['trans_result'][0]['dst']
    print('翻译的结果是: %s' % (translate_results))  # 打印翻译信息
    return translate_results
    a = 1


def leftClick(event):
    en_str = Entry1.get()
    print(en_str)
    vText = translate_word(en_str)
    Entry2.config(Entry2, text=vText)
    s.set("")
    Entry2.insert(0, vText)


def leftClick2(event):
    s.set("")
    Entry2.insert(0, "")


root = Tk()
root.title('单词翻译器')
root['width'] = 250
root['height'] = 130
Label(root, text='输入要翻译的内容:', width=15).place(x=1, y=1)
Entry1 = Entry(root, width=20)
Entry1.place(x=110, y=1)  # 输入框的显示位置
Label(root, text='翻译的结果:', width=20).place(x=1, y=20)
s = StringVar()
s.set('这是个测试')
Entry2 = Entry(root, width=20, textvariable=s)
Entry2.place(x=110, y=20)
Button1 = Button(root, text='翻译', width=8)
Button1.place(x=40, y=80)
Button2 = Button(root, text='清空', width=8)
Button2.place(x=110, y=80)
# 给button绑定鼠标监听事件
Button1.bind("<Button-1>", leftClick)
Button2.bind("<Button-1>", leftClick2)
root.mainloop()
