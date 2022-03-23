"""登录有滑块验证，没有使用ajax发送post请求
js调试过程会出现问题，鬼鬼调试工具没有问题，ASN1
"""

"""
password: HUZsk71Qv8Wi2AjcXp/xpKYvYOaCX3c2X+NYITGL8J87r8wGUFXcD4zKo1Tj3kPLFjVleoKZhCJZhDBgCHflLMD14Dp6GZVRVg++OX5dlJUOEubWhPy3WI2kl03xaF+ofM6yWhY24trNJsP1/qAAk97tWjrIS3NAqDkVOnDSwyg=
continue: 
service: passport
location: 2f736166652f
needRand: 1
isiframe: 1
logintype: normal
CSSStyle: 
autoLogin: 1
username: 123@qq.com
randimg: 00090710c2c54f098cc5fac77b56e468;fd206820e0e8480799edb19e60a7deff
isAICap: 1
readAndAgree: 1
"""
import execjs

# 获取请求表单中的pwd数据
# 1、实例化一个node对象
node = execjs.get()
# 2、打开编译js文件
js = node.compile(open('完美世界游戏个人中心.js', encoding='utf-8').read())
# 3、执行JS文件
funcName = 'pwd("{}")'.format('123465')
pwd = js.eval(funcName)
print(pwd)