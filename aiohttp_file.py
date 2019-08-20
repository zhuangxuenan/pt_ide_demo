# asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。
# 如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。
# asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。
# https://blog.csdn.net/qq_31235811/article/details/93380242
# https://www.jianshu.com/p/3de5c3626012
# https://www.cnblogs.com/ssyfj/p/9222342.html
# 使用示例, 进行一次请求

import aiohttp, asyncio
import json


# 通过协程完成了一个异步IO的get请求
# 代码必须在一个异步的函数中进行
async def main(pool=5):
    # 官方是推荐使用 aiohttp.ClientSession().get() 的，
    # 它能保证相应的资源能够得到释放。（比如保证 tcp 连接会 close）参考链接：
    # https://github.com/aio-libs/aiohttp/issues/1175#issuecomment-247330840
    # aiohttp.request会报Unclosed client session
    # 使用示例, 进行一次请求
    # async with aiohttp.request('GET', 'https://github.com') as resp:
    #    r = await resp.text()
    #    print(r)
    # ----------------------------------------------------------------------------
    # 使用示例, 进行一次请求
    # async with aiohttp.request('GET', 'https://api.github.com/events') as resp:
    #    r = await  resp.json()
    #    print(json.dumps(r))  # 将json对象或者字典转换成json字符串
    # 使用示例，进行多次请求 并限制同时请求数量

    sem = asyncio.Semaphore(pool)  # 限制同时请求的数量
    # 默认ClientSession使用的是严格模式的 aiohttp.CookieJar. RFC 2109，明确的禁止接受url和ip地址产生的cookie，
    # 只能接受 DNS 解析IP产生的cookie。可以通过设置aiohttp.CookieJar 的 unsafe=True 来配置
    jar = aiohttp.CookieJar(unsafe=True)
    # 控制同时连接的数量（连接池）
    # 同时最大进行连接的连接数为30，默认是100，limit=0的时候是无限制
    # 同一端口连接数量 limit_per_host
    conn = aiohttp.TCPConnector(limit=2,limit_per_host=30)
    async with aiohttp.ClientSession(cookie_jar=jar,connector=conn) as session:  # 给所有的请求，创建同一个session
        tasks = []
        # 列表生成式的方式初始化list
        [tasks.append(control_sem(sem, 'https://api.github.com/events?a={}'.format(i), session)) for i in
         range(10)]  # 十次请求
        await asyncio.wait(tasks)


async def control_sem(sem, url, session):  # 限制信号量
    async with sem:
        await fetch(url, session)


async def fetch(url, session):
    async with session.get(url) as resp:
        r = await resp.json()
        print(json.dumps(r))


loop = asyncio.get_event_loop()
loop.run_until_complete(main(pool=5))
print('-------------------------------------------------------------------')


# 参数
async def getparams():
    params = {'key1': 'value1', 'key2': 'value2'}
    async with aiohttp.ClientSession().get('http://httpbin.org/get', params=params) as resp:
        # 断言 格式 ： assert+空格+要判断语句+双引号“报错语句”
        assert resp.url == 'http://httpbin.org/getkey2=value2&key1=value1' '呵呵'


# 参数 表单提交
async def postparams():
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}
    headers = {'content-type': 'application/x-www-form-urlencodedit; charset=utf-8'}
    async with aiohttp.ClientSession().post(url, data=payload, headers=headers) as resp:
        r = await resp.json
        print(r)


# 参数 请求体提交
async def postparams2():
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}
    headers = {'content-type': 'application/json; charset=utf-8'}
    # json=json.dumps(payload) 将json对象处理成一个json字符串
    async with aiohttp.ClientSession().post(url, json.dumps(payload), headers=headers) as resp:
        r = await resp.json
        print(r)


# 参数 cookie
async def postparams3():
    url = 'http://httpbin.org/cookies'
    cookies = {'cookies_are': 'working'}
    async with aiohttp.ClientSession(cookies=cookies) as session:
        async with session.get(url) as resp:
            print(await resp.json)  # 不处理的话是一个json对象 不是一个json字符串


# assert resp.status == 200
# resp.headers
# await resp.text()
# await resp.text(encoding=‘gb2312’)
# await resp.read()
# await resp.json()
# await resp.content.read(10) #读取前10个字节

# 参数 上传文件
async def file_small():
    url = 'http://httpbin.org/post'
    files = {'file': open('report.xls', 'rb')}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=files) as resp:
            print(await resp.json())


# 参数 上传文件
async def file_big():
    url = 'http://httpbin.org/post'
    data = aiohttp.FormData()
    data.add_field('file',
                   open('report.xls', 'rb'),
                   filename='report.xls',
                   content_type='application/vnd.ms-excel')
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as resp:
            print(await resp.json())
