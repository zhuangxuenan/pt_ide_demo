'''
多任务可以由多进程完成，也可以由一个进程内的多线程完成。
我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。
由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，
并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
Python的标准库提供了两个模块：_thread和threading，
_thread是低级模块，threading是高级模块，对_thread进行了封装。
绝大多数情况下，我们只需要使用threading这个高级模块。
'''
import time
import threading


# 新线程的执行代码
def loop():
    print('子线程开始执行- - - -thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1;
        print('thread %s>>>%s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('子线程执行完毕- - - -thread %s ended' % threading.current_thread().name)


print('查看当前默认线程- - - -Thread %s is running....' % threading.current_thread().name)
# 创建线程的方法 传入两个参数 第一个是个函数 是子线程要执行的代码，第二个传入创建线程的名称
t = threading.Thread(target=loop, name='LoopThread')
t.start()
# join所完成的工作就是线程同步，即主线程任务结束之后，
# 进入阻塞状态，一直等待其他的子线程执行结束之后，主线程在终止
# https://www.cnblogs.com/cnkai/p/7504980.html
t.join()
print('thread %s ended' % threading.current_thread().name)
# 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，
# 主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，
# 它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，
# 我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，
# 如果不起名字Python就自动给线程命名为Thread-1，Thread-2…

# 线程锁 Lock
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，
# 互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

# 假定这是你的银行存款:
balance = 0

lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


# 由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，
# 所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现
def run_thread(n):
    # 先要获取锁:
    lock.acquire()
    try:
        for i in range(100000):
            change_it(n)
    finally:
        # 改完了一定要释放锁:
        lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
