#-*- coding: UTF-8 -*-
#使用 urllib库开发一个最简单的爬虫 爬csdn首页的html代码

from urllib import request
import  chardet

if __name__ == '__main__':
    request_url = request.Request("https://www.csdn.net")
    response = request.urlopen(request_url)
    html = response.read()
    chardet = chardet.detect(html)
    print(chardet['encoding'])
    html = html.decode(chardet['encoding'])
    print(html)
