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

d = pq(filename="temp_ui/{0}.xml".format(filename))
nodes = d('node[resource-id="com.bullet.messenger:id/number_name"]')

tasks = []

print ("开始获得x、y。。。")
for node in nodes:

        username = node.attrib['text']
        bounds = node.attrib['bounds']


        #[457,257][529,290]

        bounds_arr = bounds.replace("][",",").replace("[","").replace("]","")

        x = int(bounds_arr.split(",")[0])
        y = int(bounds_arr.split(",")[2])

        x_width = (int(bounds_arr.split(",")[2])-int(bounds_arr.split(",")[0]))/2
        y_width = (int(bounds_arr.split(",")[3])-int(bounds_arr.split(",")[1]))/2

        x_touch = int(x+x_width)
        y_touch = int(y+y_width)+48 #这个48是大致偏差，是顶部固定浮动栏的原因。

        screen = {
            "name":username,
            "x":x_touch,
            "y":y_touch
        }

        tasks.append(screen)

#print (nodes)

print ("开始执行操作。。。")

for tap in tasks:
    # print (tap)
    print ("任务名称：{0}\n屏幕坐标: x={1} y={2}".format(tap["name"],tap["x"],tap["y"]))
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
