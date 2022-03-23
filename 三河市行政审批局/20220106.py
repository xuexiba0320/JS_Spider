import requests
from fake_useragent import UserAgent
import execjs

us = UserAgent()
headers = {'Cookie': 'ICITYSession=74f3373cab08403db59bc663ba6b2bd1', 'User-Agent': us.random,}

# 执行本地的js  # 获取s、t参数
parameter = '/icity/api-v2/app.icity.guestbook.WriteCmd/getList'
result = execjs.compile(open(r"1.js").read().encode("utf-8").decode()).call('key', parameter)

# cookie = {
# 'ICITYSession':'d2e19b26db574c29a8380507c00373b7'
# }

# 翻页参数
data = {
    'OPEN@=': "1",
    'TYPE@=': "2",
    'limit': 7,
    'start': 7
}

first_url = f'http://zwfw.san-he.gov.cn{result}'
print(first_url)
response = requests.post(url=first_url, headers=headers, json=data).json()
print(response)
# with open('1.json','w',encoding='utf-8') as f:
#     f.write(response)
res = response['data'][0]["CONTENT"]
print(res)


