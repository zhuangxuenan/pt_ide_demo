#将字符转换成数字 只能转换单个字符
print(ord("账"))
#将数字转换成字符
print(chr(36134))
#把字符串变成字节 scaii或者utf-8
print("fish".encode('ascii'))
#中文不能用ascii编码 utf-8是可变长编码的Unicode
print("中文".encode("utf-8"))
#把字节变成字符串
print(b'ABC'.decode("utf-8"))
#获取字符串的长度
print(len("看看这个中文字符串的长度"))
print(len(b'ABC'))
#计算字节数 1 个中文字符经过 UTF-8 编码后通常会占用 3 个字节，而 1 个英文字符只占用 1 个字节
print(len("这个字符串的长度".encode("utf-8")))