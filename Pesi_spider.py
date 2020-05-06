import requests
import json
from requests.cookies import RequestsCookieJar

if __name__ == '__main__':
    headers = {
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    url = 'http://glzx.yonghui.cn/newvss-finance-service/vssService/OrderGoodsAction.do?method=searchOrderoodsTotal'
    cookiesstr='''
    JSESSIONID=45F83976E762E21B285F8C5B5473919D; yhTraceId=92bcf79e-da08-8285-80ac-c1dcc69ad546; yhTraceId=; sessionCode=69F35B9ECBA147C595F8450E08A58375; sessionTimeOut=604800000; signToken=5fef5789-435c-42b5-96eb-ad3da3fa8746; tokenTime=2020-02-15%2002%3A59%3A59; venderRank=1; isParper=1; venderUsingGlzxDzjsFlag=1; registerChannel=GLZX_03; isVirtual=0; uid=201704261412584736; guideFlag=N; glysBindFlag=0; glysVenderCode=20002388; glysVenderName=%u5E7F%u5DDE%u767E%u4E8B%u53EF%u4E50%u996E%u6599%u6709%u9650%u516C%u53F8; yhTraceSid=d0c23a93-6bc9-66e6-6cb8-d65ee56ed233; venderCode=20002388; venderName=%u5E7F%u5DDE%u767E%u4E8B%u53EF%u4E50%u996E%u6599%u6709%u9650%u516C%u53F8; mobilePhone=13553898596; lastTime=2018-03-07%2013%3A21%3A28; idType=1; refuseWarnFlag=0; refuseReason=; venderFlag=undefined; ssqConfirmFlag=0; ssqConfirmMenuFlag=0; verifyFlag=-1; verifyFailReason=; yhTraceUid=201704261412584736'''
    cookies_array = cookiesstr.strip().split(';')
    cookies ={}
    for cookie in cookies_array:
         cookie_ele = cookie.strip().split('=')
         cookies[cookie_ele[0]] = cookie_ele[1]
    print(cookies)
    cookie_jar = RequestsCookieJar()
    for item in cookies.items():
       cookie_jar.set(item[0],item[1],domain="glzx.yonghui.cn")


    data ={
        'appId': 'GLZX_03',
        'random': '81zXFm',
        'sign': '5acbc17b3381c15fc9b99ad858a778c1',
        'data': '{"shop": [], "orderDateStart": "2020-01-14", "orderDateEnd": "2020-02-13", "venderCode": ["20002388"], "sheetId": ""}'
    }
    response = requests.post(url,data=data,headers=headers,cookies=cookie_jar)
    result = json.loads(response.text)
    detail_url = 'http://glzx.yonghui.cn/newvss-finance-service/vssService/OrderGoodsAction.do?method=searchOrderGoodsDetail'
    good_data ={
        'appId': 'GLZX_03',
        'random': 'v5Hk6j',
        'sign': '2e69085a7760eb463ed83d944f4c231f',
        'data': '{"sheetId": "4050054749", "source": "0"}'
    }
    dresponse = requests.post(detail_url,data=good_data,headers=headers,cookies=cookie_jar)
    dresult = json.loads(dresponse.text)
    print(dresult)

    ddetail_url = 'http://glzx.yonghui.cn/newvss-finance-service/vssService/OrderGoodsAction.do?method=orderGoodsDetailGrid'
    good_data = {
        'appId': 'GLZX_03',
        'random': '3R7oPG',
        'sign': 'a0e6d1fdf0a4e7503c307dc6699f4583',
        'data': '{"sheetId": "4050054749", "source": "0"}'
    }
    ddresponse = requests.post(ddetail_url, data=good_data, headers=headers, cookies=cookie_jar)
    ddresult = json.loads(ddresponse.text)
    print(ddresult)
    print('here')

