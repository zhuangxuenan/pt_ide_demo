import asyncio

# 为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
# 请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
# 1.把@asyncio.coroutine替换为async；
# 2.把yield from替换为await。
from datetime import datetime


async def hello():
    # 打印了两行代码执行的时间，发现他们之间延迟了5秒
    print('hello world!!!', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    await asyncio.sleep(5)
    print('hello align!!!', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
