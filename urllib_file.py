from urllib import request, parse
import json

# urllib的request模块可以非常方便地抓取URL内容，
# 也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
# 这是一个GET请求
with request.urlopen('https://www.easy-mock.com/mock/5cbec5d8bfb3b05625e96633/dreamlf/urllibTest') as f:
    data = f.read()
    print('请求状态Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('请求头%s:%s' % (k, v))
    print('返回的数据data:', data.decode('utf-8'))
    print('返回的数据封装成对象:', json.loads(data.decode('utf-8')))
print('- - - - -分割线- - - - - - - -')
# 模拟浏览器发起get请求
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f2:
    data = f2.read()
    print('请求状态Status:', f2.status, f2.reason)
    for k, v in f2.getheaders():
        print('请求头%s:%s' % (k, v))
    print('返回的数据data:', data.decode('utf-8'))

# 模拟post请求
email = input('Email:')
passwd = input('passwd:')
# post请求参数
login_data = parse.urlencode([('username', email),
                              ('password', passwd),
                              ('entry', 'mweibo'),
                              ('client_id', ''),
                              ('savestate', '1'),
                              ('ec', ''),
                              ('pagerefer',
                               'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')])
req2 = request.Request('https://passport.weibo.cn/sso/login')
req2.add_header('Origin', 'https://passport.weibo.cn')
req2.add_header('User-Agent',
                'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req2.add_header('Referer',
                'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req2, login_data.encode('utf-8')) as f3:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# 通过代理访问某网站
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
# 传入一个dict
proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
oper = request.build_opener(proxy_handler, proxy_auth_handler)
with oper.open('') as f4:
    pass
