# -*- coding: UTF-8 -*-
from urllib import request
import re

if __name__ == "__main__":
    # 访问网址获取IP
    url = 'https://www.whatismyip.com/'

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    }

    # 构建request对象
request_url = request.Request(url, headers=header)

# 发送请求获取返回数据
response = request.urlopen(request_url)

# 读取相应信息并解码，并利用正则提取IP
html = response.read().decode("utf-8")
print(html)
pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
ip_list = re.findall(pattern, html)

print(ip_list[0])