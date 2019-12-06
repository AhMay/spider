#coding: utf-8
'''
爬取百度搜索前20个搜索页面的标题和链接
'''
import requests
import sys
from bs4 import BeautifulSoup as bs
import re
import chardet

headers = {
'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}

def main(keyword):
    file_name = "{}.txt".format(keyword)
    f = open(file_name,'w+', encoding='utf-8')
    f.close()
    for pn in range(0,20,10):
        params = {'wd':keyword,'pn':pn}
        response = requests.get("https://www.baidu.com/s",params=params,headers=headers)
        soup = bs(response.content,'html.parser')
        urls = soup.find_all(name='a',attrs={"href": re.compile('.')})
        for i in urls:
            if 'http://www.baidu.com/link?url=' in i.get('href'):
                a = requests.get(url=i.get('href'),headers=headers)
                print(i.get('href'))
                soup1 = bs(a.content,'html.parser')
                title = soup1.title.string
                with open(keyword+'.txt','r',encoding='utf-8') as f:
                    if a.url not in f.read():
                        f = open(keyword+'.txt','a',encoding='utf-8')
                        f.write(title + '\n')
                        f.write(a.url + '\n')
                        f.close()

if __name__ == '__main__':
    keyword ='Django'
    main(keyword)
    print("下载完成")
    # if len(sys.argv) != 2:
    #     print("no keyword")
    #     print("please enter keyword")
    #     sys.exit(-1)
    # else:
    #     main(sys.argv[1])
    #     print("下载完成")
