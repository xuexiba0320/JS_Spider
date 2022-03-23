import json

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Mobile Safari/537.36'}

url_1 = 'https://fanyi.baidu.com/?aldtype=16047'
response1 = requests.get(url=url_1, headers=headers)

url_2 = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"

data = {
    'from': 'zh',
    'to': 'en',
    'query': '你',
    'transtype': 'enter',
    'simple_means_flag': '3',
    'sign': '621118.891151',
    'token': '3408d0d14d778cdaebf694aab2c3dec5',
    'domain': 'common', }

response = requests.post(url=url_2, headers=headers, data=data)
res = response.content
res_dict = json.loads(res)
# trans = res_dict['trans_result']
print(res_dict)
