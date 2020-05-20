# translate_tet.py
from tkinter import Label, Tk, Entry, Button, StringVar


def demo_tk():
    root = Tk()
    root.title('单词翻译器')
    root['width'] = 250
    root['height'] = 130
    Label(root, text='输入要翻译的内容:', width=15).place(x=1, y=1)

    Entry1 = Entry(root, width=20)
    Entry1.place(x=110, y=1) # 输入框的显示位置

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
    # Button1.bind("<Button-1>", leftClick)
    # Button2.bind("<Button-1>", leftClick2)

    root.mainloop()


if __name__ == "__main__":
    demo_tk()
