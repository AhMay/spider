#-*- coding: UTF-8 -*-
#使用 urllib库开发一个最简单的爬虫 爬csdn首页的html代码

from urllib import request
from urllib import parse
import time
import random
import hashlib
import json
import  chardet

'''使用urlopen(request_url,data)发送参数'''

if __name__ == '__main__':
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    header = {
                 'Accept': 'application / json, text / javascript, * / *; q = 0.01',
    'Accept - Encoding': 'gzip, deflate',
    'Accept - Language': 'zh - CN, zh;q = 0.9',
    'Connection': 'keep - alive',
    'Content - Length': 251,
    'Content - Type': 'application / x - www - form - urlencoded;charset = UTF - 8',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http: // fanyi.youdao.com',
    'Referer': 'http: // fanyi.youdao.com /',
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 73.0.3683.86 Safari / 537.36',
    'X - Requested - With': 'XMLHttpRequest',
    }
    i = input("Translation for: ")
    client = "fanyideskweb"
    t = str(int(time.time()*1000))
    salt = t+ str(random.randint(1,10))
    c ='n%A-rKaT5fb[Gy?;N5@Tj'
    md5 = hashlib.md5()
    md5.update(client.encode('utf-8'))
    md5.update(i.encode('utf-8'))
    md5.update(salt.encode('utf-8'))
    md5.update(c.encode('utf-8'))

    sign = md5.hexdigest()
    print(salt)
    print(t)
    print(sign)
    data = {
        'i': i,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client':client,
        'salt': salt,
        'sign': sign,
        'ts':   t,
         'bv': '140f03b6cc43b5b1fabe089d78dc366f',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME',
    }

    #使用parse方法对参数进行URL编码
    data = parse.urlencode(data).encode('utf-8')
    #使用urllib发送POST数据无需拼接URL
    request_url = request.Request(url,data=data,headers=header)
    response = request.urlopen(request_url)
    print(response.getcode()) #200 表示成功
    json_result = json.load(response)
    print(json_result)
    translation_result = json_result['translateResult'][0][0]['tgt']
    print("翻译的结果是：%s" % translation_result)
    # html = response.read()
    # chardet = chardet.detect(html)
    # print(chardet['encoding'])
    # html = html.decode(chardet['encoding'])
    # print(html)

    import  urllib.error
    try:
        urllib.request.urlopen('htt://www.baidu.com')
    except urllib.error.URLError as e:
        print(e.reason)

    try:
        urllib.request.urlopen('http://www.baidu.com/admin')
    except urllib.error.HTTPError as e1:
        print(e1.reason)
        print(e1.code)