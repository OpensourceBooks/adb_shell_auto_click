from pyquery import PyQuery as pq
from os import popen
from time import sleep

d = pq(filename="temp_ui/你得到的文件.xml")
nodes = d("node")

screen_taps = []

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
        y_touch = int(y+y_width)

        screen = {
            "x":x,
            "y":y
        }

        screen_taps.append(screen)

for tap in screen_taps:
    # print (tap)
    popen("adb shell input tap {0} {1}".format(tap["x"],tap["y"]))
    sleep(10)
    popen("adb shell input keyevent {0}".format(4))
