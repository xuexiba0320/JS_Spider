"""不需要js逆向获取得到请求的密匙：进入网站会发起一个请求，响应中返回密匙"""
import requests
from fake_useragent import UserAgent
import re


def get_keyword():
    first_url = 'http://www.zjmazhang.gov.cn/hdjlpt/published?via=pc'
    res = requests.get(url=first_url, headers={'User-Agent': UserAgent().random})
    # print(res.text)
    # 请求初始网页，正则得到token
    token = re.findall("var _CSRF = '(.*?)';", res.text)[0]
    print(token)
    # 得到Cookie：session
    cookie = res.cookies['szxx_session']
    print(cookie)
    return token, cookie


def get_data():
    token, cookie = get_keyword()
    # 请求头
    headers = {
        'User-Agent': UserAgent().random,
        'X-CSRF-TOKEN': token,
        # cookie 中包含szxx_session
        'Cookie': 'szxx_session='+cookie
    }

    # data表单数据一定要添加不然无法访问接口获取数据
    data = {
            'offset': 0,
            'limit': 20,
            'site_id': '759010'

    }
    # 数据接口
    url = 'http://www.zjmazhang.gov.cn/hdjlpt/letter/pubList'

    response = requests.post(url=url, headers=headers, data=data)
    print(response.text)


if __name__ == '__main__':
    get_data()
    # get_keyword()