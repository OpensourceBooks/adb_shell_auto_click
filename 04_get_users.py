from os import popen
from time import sleep
from time import time
from pyquery import PyQuery as pq
import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = str(int(time()))
#把当前的屏幕控件保存到手机的sd卡
print ("正在截屏。。。")

popen("adb shell screencap -p /sdcard/{0}.png".format(filename))

print ("正在保存截屏。。。")
#延时2秒钟，确保xml已经保存
sleep(3)
print ("正在复制到PC端项目文件夹temp_ui中。。。")
#把xml文件保存在项目的temp_ui目录
popen("adb pull /sdcard/{0}.png temp_ui".format(filename))

sleep(5)

tasks=[]
#载入并显示图片
img=cv2.imread("temp_ui/{0}.png".format(filename))
cv2.imshow('img',img)
#灰度化
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#输出图像大小，方便根据图像大小调节minRadius和maxRadius
print(img.shape)
#霍夫变换圆检测
circles= cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=30,minRadius=5,maxRadius=300)
#输出返回值，方便查看类型
print(circles)
#输出检测到圆的个数
print(len(circles[0]))

print('-------------我是条分割线-----------------')
#根据检测到圆的信息，画出每一个圆
for circle in circles[0]:
    #圆的基本信息
    print(circle[2])
    #坐标行列
    x=int(circle[0])
    y=int(circle[1])
    #半径
    r=int(circle[2])
    #在原图用指定颜色标记出圆的位置
    #img=cv2.circle(img,(x,y),r,(0,0,255),-1)




    screen = {
        "x":x,
        "y":y
    }
    tasks.append(screen)

#print (nodes)

print ("开始执行操作。。。")

for tap in tasks:
    # print (tap)
    print ("正在点击 x={0} y={1}".format(tap["x"],tap["y"]))
    popen("adb shell input tap {0} {1}".format(tap["x"],tap["y"]))
    sleep(5)
    print("人物页面完成")

    # 是否是好友
    filename = str(int(time()))
    popen("adb shell uiautomator dump /sdcard/profile_{0}.xml".format(filename))

    print ("正在保存屏幕控件profile_xml文件。。。")
    #延时2秒钟，确保xml已经保存
    sleep(3)
    print ("正在复制profile_xml到PC端项目文件夹temp_ui中。。。")
    #把xml文件保存在项目的temp_ui目录
    popen("adb pull /sdcard/profile_{0}.xml temp_ui".format(filename))
    sleep(5)
    print("正在检查是否是好友")
    d_profile = pq(filename="temp_ui/profile_{0}.xml".format(filename))

    #得到的是数组，即便是1个。
    query = d_profile('node[text="添加到联系人"]')

    #如果是陌生人
    if query:


        #点击添加到联系人
        print("不是好友，准备添加到联系人")
        popen("adb shell input tap {0} {1}".format(360,650))#这个数字是测试时测试出来的，不同的手机分辨率不一样。
        #发送申请
        print ("确认申请")
        sleep(2)
        popen("adb shell input tap {0} {1}".format(600,550))#这个数字是测试时测试出来的，不同的手机分辨率不一样。
        sleep(3)

    print ("返回")
    popen("adb shell input keyevent {0}".format(4))
    sleep(5)
