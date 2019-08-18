import requests

# Python内置的urllib模块，用于访问网络资源。但是，
# 它用起来比较麻烦，而且，缺少很多实用的高级功能。
# 更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便
# 需要传入HTTP Header时，我们传入一个dict作为headers参数：
r = requests.get('https://www.douban.com/')
print(r.status_code)  # 得到请求状态码 200 500 403
print('--------------------------分割线-----------------------------')
# print(r.text)  # 得到响应数据
print('--------------------------分割线-----------------------------')
print(r.ok)  # 根据不同的状态码返回True或者False
print('--------------------------分割线-----------------------------')
print(r.content)  # 响应数据 以字节形式返回
print('--------------------------分割线-----------------------------')
# 如果返回的数据是json的话 可以使用.json() 如果响应数据不是json的话不要使用这个函数
# print(r.json())
print(r.headers)  # 获取请求头信息
print('--------------------------参数分割线-----------------------------')
# 带参数的URL，传入一个dict作为params参数：
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)  # 实际请求的url
print(r.status_code)
print(r.content)
print('--------------------------请求头分割线-----------------------------')
# 需要传入HTTP Header时，我们传入一个dict作为headers参数：
r = requests.get(
    'https://www.douban.com/',
    headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
)
print(r.url)  # 实际请求的url
print(r.status_code)
print(r.text)
print(r.content)
print('--------------------------post分割线-----------------------------')
# post 表单请求 application/x-www-form-urlencoded
r = requests.post('https://accounts.douban.com/login',
                  data={'form_email': 'abc@example.com', 'form_password': '123456'},
                  headers={'Content-Type': 'application/x-www-form-urlencodedit; charset=utf-8'})
print(r.url)  # 实际请求的url
print(r.status_code)
print(r.text)
print(r.content)
# 如果post请求不是以表单的方式提交的参数而是json请求体
# 内部自动序列化为JSON
# r = requests.post('url', json={'key': 'value'}, headers={'Content-Type': 'application/json; charset=utf-8'})

# 上传文件
# upload_files = {'file': open('文件路径', 'rb')}
# r = requests.post('url', files=upload_files)

# 传入cookie
cs = {'token': '12345', 'status': 'working'}
r = requests.get('url', cookies=cs)

# 通过阅读源码我们知道 不论是get还是post方法
# 最后实际上调用的都是：request(method, url, **kwargs)
# 所以也可以这么调用：
# requests.request('get', 'url', data={}, headers={}, cookies={})
# requests.request('post', 'url', params={}, headers={}, cookies={})
# requests.request('post', 'url', json={}, headers={}, cookies={})
# requests.request('post', 'url', files={})
# dict_s = dict(params={}, headers={}, cookies={})
# requests.request('post', 'url', **dict_s)
