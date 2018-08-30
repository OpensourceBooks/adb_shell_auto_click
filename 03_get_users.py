from os import popen
from time import sleep
from time import time
from pyquery import PyQuery as pq

filename = str(int(time()))
#把当前的屏幕控件保存到手机的sd卡
print ("正在获取屏幕控件。。。")

popen("adb shell uiautomator dump /sdcard/{0}.xml".format(filename))

print ("正在保存屏幕控件xml文件。。。")
#延时2秒钟，确保xml已经保存
sleep(3)
print ("正在复制到PC端项目文件夹temp_ui中。。。")
#把xml文件保存在项目的temp_ui目录
popen("adb pull /sdcard/{0}.xml temp_ui".format(filename))

sleep(5)

d = pq(filename="temp_ui/{0}.xml".format(filename))
nodes = d("node")

tasks = []

print ("开始获得x、y。。。")
for node in nodes:
    # 找到包含人员的
    if node.attrib['resource-id']=="com.bullet.messenger:id/number_name":
        username = node.attrib['text']
        bounds = node.attrib['bounds']


        #[457,257][529,290]

        bounds_arr = bounds.replace("][",",").replace("[","").replace("]","")

        x = int(bounds_arr.split(",")[0])
        y = int(bounds_arr.split(",")[2])

        x_width = (int(bounds_arr.split(",")[2])-int(bounds_arr.split(",")[0]))/2
        y_width = (int(bounds_arr.split(",")[3])-int(bounds_arr.split(",")[1]))/2

        x_touch = int(x+x_width)
        y_touch = int(y+y_width)+20 #这个20是大致偏差，可能是固定浮动栏的原因。

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
    print ("返回")
    popen("adb shell input keyevent {0}".format(4))
