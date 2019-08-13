from io import StringIO, BytesIO
import os
# 读写操作可以在磁盘中进行也可以在内存中进行
# 可以在内存中读写的有两种 分别是StringIO和BytesIO
# 顾名思义 分别用来往内存中写入str和二进制文件的
try:
    # 读
    with StringIO('Hello!\nHi!\nGoodbye!') as f:
        for line in f.readlines():
            print(line)
    # 写
    with StringIO() as f2:
        f2.write('Hello')
        f2.write('\t')
        f2.write('World')
        f2.write('\n')
        f2.writelines(['111', '222', '333', '444', '555'])  # 此函数传入一个要写入文件的字符串序列。 可以是一个list[] 也可以是一个tuple
        print(f2.getvalue())
    # 写
    with BytesIO() as f3:
        f3.write('中文'.encode('utf-8'))
        print(f3.getvalue())
    # 读
    with BytesIO(b'\xe4\xb8\xad\xe6\x96\x87') as f4:
        print(f4.read().decode('utf-8'))
    print(os.name)
    print(os.uname())
except IOError as e:
    print('except:', e)
finally:
    print('可他妈搞完了')
