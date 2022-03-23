import hashlib
import random
import re
import time

import requests


class YouDao(object):
    def __init__(self, word):
        self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400',
            'Referer': 'https://fanyi.youdao.com/',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1925509054@10.108.160.102; JSESSIONID=aaatBpyxa1N4c96DvNr1x; OUTFOX_SEARCH_USER_ID_NCOO=1869358598.1847198; ___rl__test__cookies=1637752208672'
        }
        self.word = word

    def run(self):
        # url
        # headers
        # formdata
        # 发送请求获取响应  # 解析数据
        self.parse_data()

    def generate_formdata(self):
        # 表单中变化的数据如下:
        """     i: 你好
                salt: 16377667618397
                sign: 075b835377ff9e53b3833108e15eca68
                lts: 1637766761839
        """
        # 模拟JS生成表单参数
        # r = "" + (new Date).getTime() -> lts=r
        lts = str(int(time.time() * 1000))
        # i = r + parseInt(10 * Math.random(), 10) -> salt=i
        salt = lts + str(random.randint(0, 9))
        # sign: n.md5("fanyideskweb" + e + i + "Y2FYu%TNSbMCxc3t2u^XT")
        sign_data = "fanyideskweb" + self.word + salt + "Y2FYu%TNSbMCxc3t2u^XT"
        # hash算法处理
        #    创建hash对象
        md5 = hashlib.md5()
        #    向hash对象中添加需要做hash运算的字符串
        #    注意：需要将字符串编码成二进制格式
        md5.update(sign_data.encode())
        # 获取字符串的hash值
        sign = md5.hexdigest()
        form_data = {
            'i': self.word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'lts': lts,
            'bv': '03a6a27012b22bc3c7ecc76381772182',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        return form_data

    def parse_data(self):
        # 获取表单
        formdata = self.generate_formdata()
        response = requests.post(url=self.url, headers=self.headers, data=formdata)
        self.save_data(response.content.decode('utf-8'))
        # print(response.content.decode('utf-8'))

    def save_data(self, data_json):
        data = data_json
        # 通过正则提取出翻译结果
        result_data = re.findall('"tgt":"(.*?)"', data)[0]
        print('翻译结果=》', result_data)


if __name__ == '__main__':
    print('中英互译')
    keyword = input("翻译单词=》 ")
    youdao = YouDao(keyword)
    youdao.run()
