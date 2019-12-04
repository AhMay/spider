#-*- coding: UTF-8 -*-
#使用 urllib库开发一个最简单的爬虫 爬csdn首页的html代码

from urllib import request

if __name__ == '__main__':
    response = request.urlopen("https://www.csdn.net/")
    html = response.read()
    html = html.decode('utf-8')
    print(html)
