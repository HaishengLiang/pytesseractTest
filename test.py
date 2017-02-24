#coding=utf-8
import sys
from PIL import Image, ImageEnhance
from pytesseract import *

img = Image.open(sys.argv[1]) # 读入图片

#亮度修正0-1
img = ImageEnhance.Brightness(img).enhance(3)
#锐度修正0-1
#img = ImageEnhance.Sharpness(img).enhance(0.2)
#对比度修正0-1
img = ImageEnhance.Contrast(img).enhance(2)
#将彩色图像转化为灰度图
img = img.convert("L")

def binarizing(img,threshold): #input: gray image
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img

img = binarizing(img,200)
#img = depoint(img)

#保存图片
img.save("input-black.png", "PNG")
#弹出图片
#img.show()
print image_to_string(img)
 
# #放大图像 方便识别
# im_orig = Image.open('input-black.png')
# big = im_orig.resize((1000, 500), Image.NEAREST)
