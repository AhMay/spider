#-*- coding: UTF-8 -*-
#使用 urllib库开发一个最简单的爬虫 爬csdn首页的html代码

from urllib import request
import urllib.parse
import  chardet

if __name__ == '__main__':
    url = "https://so.csdn.net/so/search/s.do"
    params = {'q':'大江狗',}
    header = {
        "User-Agent": " Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    }
    #使用parse方法对参数进行URL编码
    encoded_params = urllib.parse.urlencode(params)
    #拼接后的request地址
    request_url = request.Request(url+"?"+encoded_params,headers=header)
    response = request.urlopen(request_url)
    html = response.read()
    chardet = chardet.detect(html)
    print(chardet['encoding'])
    html = html.decode(chardet['encoding'])
    print(html)
