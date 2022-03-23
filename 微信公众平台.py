"""登录需要滑块验证
模拟登录后会有扫描验证，暂时无法直接使用接口进行模拟登陆。
"""
import requests
import execjs
from fake_useragent import UserAgent
FormDate = {
    """
    username: 132@qq.com
    pwd: e10adc3949ba59abbe56e057f20f883e
    imgcode: 
    f: json
    userlang: zh_CN
    redirect_url: 
    token: 
    lang: zh_CN
    ajax: 1
"""
}

username = input('请输入账户名:')
pwd = input('请输入密码:')

# 获取请求表单中的pwd数据
# 1、实例化一个node对象
node = execjs.get()
# 2、打开编译js文件
js = node.compile(open('微信公众平台.js', encoding='utf-8').read())
# 3、执行JS文件
funcName = 'getPwd("{}")'.format(pwd)
pwd = js.eval(funcName)
print(pwd)

url = 'https://mp.weixin.qq.com/cgi-bin/bizlogin?action=startlogin'
headers = {
            'User-Agent': UserAgent().random,
            'referer': 'https://mp.weixin.qq.com/',
            'Cookie': 'ua_id=bIDWCnEm5IVFDMSDAAAAALTJ2jDLdSUrTMDD8zE0y1o=; wxuin=41997229999123; cert=BXekb7bwtjQrh2P9sCNZWLiCKdhKlRCa; sig=h01dd0fb01bc575627d34eb7697a1609b3a34d45ff9916e04b3fb4a2165a73d554cb40ea47513a7e41b; ticket_uin=3919169497; login_certificate=KcCMO7CEGvpLwY3PcE3uhBzuiUdo46OXyNMAnOppmPQ=; ticket_certificate=OnDNXxgL1x3IpeUlxpV/KU8eHL7i15vQ6r02l++g2ro=; fake_id=3919169497; login_sid_ticket=5d0aae00cee371752a6931128e83a1e8bd5125fb; noticeLoginFlag=1; uuid=60d9b6fe9c9167aabc9d497a54e2c15'}
data = {
        'username': username,
        'pwd': pwd,
        'imgcode': '',
        'f': 'json',
        'userlang': 'zh_CN',
        'redirect_url': '',
        'token': '',
        'lang': 'zh_CN',
        'ajax': '1',
}
response = requests.post(url=url, headers=headers, data=data)
print(response.text)

