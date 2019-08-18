import chardet

# 本类主要用来检测字符编码
print(chardet.detect(b'Hello, world!'))
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))
data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))
print(chardet.detect('离离原上草，一岁一枯荣'.encode()))  # 默认转码就是utf-8
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))
