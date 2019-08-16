import base64, hashlib, hmac

# 各种加密 解密
# base64
# 加密的时候可以传入 字符串 二进制数据比如字节
a1 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')  # 加密
a2 = base64.urlsafe_b64decode(a1)  # 解密
print(a1)
print(a2)
b1 = base64.urlsafe_b64encode('choushabi'.encode('utf-8'))
b2 = base64.urlsafe_b64decode(b1).decode('utf-8')
print(b1)
print(b2)

print('- - - - - - -分割线- - - - - - —')

# md5
md5 = hashlib.md5()
# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

print('- - - - - - -分割线- - - - - - —')

sha1 = hashlib.sha1()
# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
sha1.update('how to use md5 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

print('- - - - - - -分割线- - - - - - —')

# Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
# 和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。
# 采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
# Python自带的hmac模块实现了标准的Hmac算法。我们来看看如何使用hmac实现带key的哈希。
# 传入的key和message都是bytes类型，str类型需要首先编码为bytes
h = hmac.new(b'666', 'python hashlib?'.encode('utf-8'), digestmod='MD5')
h.update('python hashlib?'.encode('utf-8'))
print(h.hexdigest())
