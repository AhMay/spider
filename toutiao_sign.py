import time
import hashlib
def get_as_cp():  # 该函数主要是为了获取as和cp参数，程序参考今日头条中的加密js文件：home_4abea46.js
    zz = {}
    now = round(time.time())
    print(now) # 获取当前计算机时间
    e = hex(int(now)).upper()[2:] #hex()转换一个整数对象为16进制的字符串表示
    print('e:', e)
    a = hashlib.md5()  #hashlib.md5().hexdigest()创建hash对象并返回16进制结果
    print('a:', a)
    a.update(str(int(now)).encode('utf-8'))
    i = a.hexdigest().upper()
    print('i:', i)
    if len(e)!=8:
        zz = {'as':'479BB4B7254C150',
        'cp':'7E0AC8874BB0985'}
        return zz
    n = i[:5]
    a = i[-5:]
    r = ''
    s = ''
    for i in range(5):
        s= s+n[i]+e[i]
    for j in range(5):
        r = r+e[j+3]+a[j]
    zz ={
    'as':'A1'+s+e[-3:],
    'cp':e[0:3]+r+'E1'
    }
    print('zz:', zz)
    return zz