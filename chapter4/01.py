# urllib_test-1.py

from urllib import request


def case1():
    response = request.urlopen('http://fanyi.baidu.com')
    html = response.read()
    html = html.decode('utf-8')  # decode() 将网页的信息进行编码, 否则会产生乱码
    print(html)


def case2():
    # Request 对象
    req = request.Request('http://fanyi.baidu.com')
    response = request.urlopen(req)
    html = response.read()
    html = html.decode('utf-8')  # decode() 将网页的信息进行编码, 否则会产生乱码
    print(html)


def case3():
    """ 获取服务器响应信息 """
    f = request.urlopen('http://fanyi.baidu.com')
    data = f.read()
    print('Status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))


def case4():
    """
    使用Response对象的geturl()方法 info()方法 getcode()方法
    获取相关的URL响应信息和响应HTTP状态码
    """
    req = request.Request('http://fanyi.baidu.com')
    response = request.urlopen(req)
    print("geturl打印信息: %s" % (response.geturl()))
    print('---------------------------------------')
    print("info打印信息: %s" % (response.info()))
    print('---------------------------------------')
    print("getcode: %s" % (response.getcode()))


def case5():
    """ 使用UserAgent 方法一 """
    url = 'http://www.csdn.net/'
    head = {}
    # 写入User Agent的值
    head['User-agent'] = 'Mozilla/5.0(Linux;Android 4.1.1;Nexus 7 Build/JR003D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166Safari/535.19'
    req = request.Request(url, headers=head)  # 创建Request对象
    response = request.urlopen(req)  # 传入创建好的Request对象
    html = response.read().decode('utf-8')  # 读取响应信息并编码
    print(html)


def case6():
    """ 使用UserAgent 方法一 """
    url = 'http://www.csdn.net/'
    req = request.Request(url)
    # 传入headers
    req.add_header('User-Agent',
                   'Mozilla/5.0(Linux;Android 4.1.1;Nexus 7 Build/JR003D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166Safari/535.19'
                   )
    response = request.urlopen(req)
    html = response.read().decode('utf-8')  # 读取响应信息并编码
    print(html)


if __name__ == "__main__":
    # case1()
    # case2()
    # case3()
    # case4()
    # case5()
    case6()
