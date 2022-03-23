"""Steam密码加密JS逆向
"""
# 表单型式
import execjs

FormData = {
    """
    donotcache: 1642149161795
    password: YWrGn3SLho+vNiNQU11LeXzlRTd02jtkoh5UriFPk4DZ8qDM/wMNuqYlJy2DRLY1RvLL3dYFTXsC9Im3aQ800oJyY5g8rXm6KQviI3lZO8+XeU8Tk8Y5kEJIlVWtnvx9JqA29DsHIumY1kPjW7TTsSnNja3hsTI+cUJz/JmJuoBQCg/vleSm3rI7DLr1UW4ecYroy8Mi3up7VPoSzqUMyx5T563CsgGz5/zQS/FbFzxVSBphjBPo7WEzV9LlyQwtbMRC/3h2Se/saSgikJ5ERYwKqyZHybRiWP4KiglI+2TehWW4o0QVFZGhFZn4t+UcDg6BSXA8AYsbcEUlLWpzjQ==
    username: 2585563315
    """
}
url = 'https://store.steampowered.com/login/dologin/'
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'}

# 明文密码
password = '123456'
# 获取加密后的密码
def main():
    # 1、实例化一个node对象
    node = execjs.get()
    # 2、打开JS加密算法代码
    js = node.compile(open('Steam.js', encoding='utf-8').read())
    # 3、执行JS文件
    funcName = f'getPassword({password})'
    pwd = js.eval(funcName)
    print(pwd)


if __name__ == '__main__':
    main()
