import execjs

# 执行本地的js
parameter = '/icity/api-v2/app.icity.guestbook.WriteCmd/getList'
result = execjs.compile(open(r"1.js").read().encode("utf-8").decode()).call('key', parameter)
print(result)

print(execjs.get().name)  # 查看调用环境
e = execjs.eval('a = new Array(1, 2, 3)')  # 可以直接执行 JS 代码
print(e)

