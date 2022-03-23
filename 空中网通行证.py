"""https://passport.kongzhong.com/login"""
import time
import requests
import execjs
import re


def headers():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Referer': 'https://passport.kongzhong.com/'
    }
    return headers

def encrypt(pwd):
    timec = int(time.time() * 1000)
    url = f'https://sso.kongzhong.com/ajaxLogin?j=j&jsonp=j&service=https://passport.kongzhong.com/&_={timec}'
    result = requests.get(url=url, headers=headers()).text
    DC = re.findall('"dc":"(.*?)"', result)[0]
    print('加密密匙为:', DC)
    # 1、实例化一个node对象
    node = execjs.get()
    # 2、打开JS加密算法代码
    js = node.compile(open('空中网通行证.js', encoding='utf-8').read())
    # 3、执行JS文件
    funcName = 'pwd("{}","{}")'.format(pwd, DC)
    pwd = js.eval(funcName)
    print('加密后的密码:', pwd)
    return pwd


def login():
    username = '1807879xxxx'
    password = 'xuexxxxxx'
    timec = int(time.time() * 1000)
    # 获取加密后的密码
    encrypt_password = encrypt(password)

    login_url = 'https://sso.kongzhong.com/ajaxLogin'
    params = {
        'j': 'j',
        'type': '1',
        'service': 'https://passport.kongzhong.com/',
        'username': username,
        'password': encrypt_password,
        'vcode': '',
        'toSave': '0',
        '_': timec
    }

    # 模拟登录请求
    response = requests.get(url=login_url, params=params, headers=headers())
    print(response.status_code)


if __name__ == '__main__':
    login()

