import time
import hashlib
import math
import requests
import json
def getHoney():
    t =math.floor(int(time.time()))
    e = hex(t).upper()[2:]
    md5 = hashlib.md5()
    md5.update(str(t).encode('utf-8'))
    i = md5.hexdigest().upper()
    if (len(e) != 8):
        return {
            'as': "479BB4B7254C150",
            'cp': "7E0AC8874BB0985"
        }
    n = i[0:5]
    s = i[-5:]
    o=''
    for a in range(0,5):
        o+=n[a] + e[a]
    r=''
    for l in range(0,5):
        r += e[l+3] + s[l]

    return {
        'as': 'A1' + o + e[-3:],
        'cp': e[0:3] + r + 'E1'
    }

if __name__ == '__main__':
    headers = {
        'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'referer': 'https://www.toutiao.com/ch/news_hot/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    cookies = {
    'tt_webid':'6767234880972555784'
    }
    params = {
        'utm_source':'toutiao',
        'widen':1,
        'max_behot_time':0,
        'max_behot_time_tmp':0,
        'tadrequire':'true',
    # as=A1F59D9F4199DF2
    # cp=5DF1C96DFF926E1
     #'_signature':0
    }
    as_cp = getHoney()
    params['as'] = as_cp['as']
    params['cp'] = as_cp['cp']
    url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot'
    #utm_source=toutiao
    # widen=1
    # max_behot_time=0
    # max_behot_time_tmp=0
    # tadrequire=true
    # as=A1F59D9F4199DF2
    # cp=5DF1C96DFF926E1
    # _signature=OG-WjAAgEBnKQKTLdP8hpjhvl5AAGWk'

    response = requests.get(url=url,params=params,headers=headers,cookies=cookies)
    data = json.loads(response.text)
    print(data['data'])