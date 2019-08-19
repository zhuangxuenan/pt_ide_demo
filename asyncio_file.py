import asyncio
import threading


# @asyncio.coroutine把一个generator标记为coroutine类型，
# 然后，我们就把这个coroutine扔到EventLoop中执行。
# hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
# 由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，
# 而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，
# 线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。
# 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，
# 而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
print('- - - - - - - - - - - - - - - - - - - - - - - -')


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
