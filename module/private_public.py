#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 正常的函数和变量名是公开的（public），可以被直接引用，比如： abc ，x123 ， PI 等；
# 类似 _xxx 和 __xxx 这样的函数或变量就是非公开的（private），不应该被直接引用，比如 _abc ， __abc 等
im = Image.open('D:\py_img\img.jpg')
# 获取图片尺寸
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%
im.thumbnail((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))
# 把缩放后的图像用jpeg格式保存:
im.save('D:\py_img\haha.jpg', 'jpeg')
# 图片模糊
im2 = im.filter(ImageFilter.BLUR)
im2.save('D:\py_img\mohu.jpg', 'jpeg')
print('-------------------------')


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('D:\py_img\hhest.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('D:\py_img\code.jpg', 'jpeg')
# https://www.cnblogs.com/Lival/p/6211602.html
# https://www.cnblogs.com/homelessdog/p/10208090.html
