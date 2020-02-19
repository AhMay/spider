'''
百事的一些公共函数和常数
'''
import math
import random
from collections import OrderedDict

appId = 'GLZX_03'
order_sheet_name ="到货汇总"
detail_sheet_name = "到货情况明细"
logon_url ="http://glzx.yonghui.cn/newvssportal/login.html" #登录首页
order_url = "http://glzx.yonghui.cn/newvss-finance-service/vssService/OrderGoodsAction.do?method=searchOrderoodsTotal" #订货到货查询页面
order_huizong_url = "http://glzx.yonghui.cn/newvss-finance-service/vssService/OrderGoodsAction.do?method=searchOrderGoodsDetail" #到货汇总查询页面
order_grid_url ="http://glzx.yonghui.cn/newvss-finance-service/vssService/OrderGoodsAction.do?method=orderGoodsDetailGrid" #到货情况明细
vender_url = "http://glzx.yonghui.cn/newvss/vssService/VenderManagerAction.do?method=getVenderList" #一个账户下的供应商列表
vender_switch_url = "http://glzx.yonghui.cn/newvssportal/venderCenter/new_user_center.html" #切换供应商
vender_sheet ={
        'venderCode':"供应商代码",
        'venderName':"供应商名称",
}

order_sheet_headers ={
        "订货日期":"checkdate",
        "订单编号": "sheetid",
        "供应商编码":"venderid",
        "供应商名称":"vendername",
        "门店号":"shopid",
        "门店名称":"shopname",
        "订货人":"checker",
        "订货品项数":"purchasecount",
        "到货品项数":"receiptcount",
        "品项到库率(%)":"qtyrate",
        "订单总额":"purchasevalue",
        "到库总额":"receiptvalue",
        "供货满足率(%)":"valuerate"
}

order_sheet_headers = OrderedDict(order_sheet_headers)

order_grid_sheet_headers ={
        "订货编号":"sheetid",
        "商品编码":  "goodsid",
        "商品条码":"barcode",
        "商品名称":"goodsname",
        "规格":"spec",
        "销售单位":"unitname",
        "含税进价":"cost",
        "订货数量":"qty",
        "到库数量":"rcvqty",
        "进价金额":"costvalue",
}
order_grid_sheet_headers = OrderedDict(order_grid_sheet_headers)
headers = {
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

#随机数
def randomWord(randomFlag,min,max=0):
    s_tr = ''
    s_range=min
    arr=['0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            'a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z',
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z']
    if(randomFlag):
        s_range = round(random.random()*(max-min))+min

    for i in range(0,s_range):
        pos = round(random.random()* (len(arr)-1))
        s_tr +=arr[pos]
    return s_tr

def get_sign(appId,rand_str,signToken):
    sign_str = appId + rand_str[2:5] +signToken
    import hashlib
    md5 = hashlib.md5()
    md5.update(sign_str.encode('utf-8'))
    sign = md5.hexdigest()
    return sign
