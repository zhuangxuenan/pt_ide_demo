#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = '哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈'
try:
    # 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
    # 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
    # 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
    # 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，
    # 每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
    # 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；
    # 如果是配置文件，调用readlines()最方便：
    # 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，
    # 还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
    # StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
    # 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
    # 因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()
    # 函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
    # 'r' open for reading(default)
    # 'w' ope for writing, truncating the file first
    # 'x' open for exclusive creation, failing if the file already exists
    # 'a' open for writing, appending to the end of the file if it exists
    # 'b' binary mode
    # 't' text mode(default)
    # '+ open a disk file for updating(reading and writing)
    with open('D:\py_img\cashi.txt', 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            print(line.strip())  # 把末尾的'\n'删掉
    # 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。
    # 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
    with open('D:\py_img\haha.jpg', 'rb')as f2:
        print(f2.read())
    # 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
    # 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。
    # 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
    with open('D:\py_img\kankan.txt', 'w', encoding='utf-8') as f3:
        f3.write(s)
except FileNotFoundError as e:
    print('except:', e)
finally:
    print('呵呵 终于弄完了----')
