from pyquery import PyQuery as pq
from os import popen
from time import sleep

# f = open("temp_ui/1535618324.xml","r")
# centent = f.readlines()
# f.close()
# d = pq(centent)
d = pq(filename="temp_ui/profile_1535630001.xml")

#得到的是数组，即便是1个。
query = d('node[text="添加到联系人"]')

#如果是陌生人
if query:


    #点击添加到联系人
    popen("adb shell input tap {0} {1}".format(360,500))#这个数字是测试时测试出来的，不同的手机分辨率不一样。
    #发送申请
    print ("确认申请")
    sleep(2)
    popen("adb shell input tap {0} {1}".format(600,500))#这个数字是测试时测试出来的，不同的手机分辨率不一样。


# screen_taps = []
#
# for node in nodes:
#     # 找到包含人员的
#     if node.attrib['resource-id']=="com.bullet.messenger:id/number_name":
#         username = node.attrib['text']
#         bounds = node.attrib['bounds']
#
#         #[457,257][529,290]
#
#         bounds_arr = bounds.replace("][",",").replace("[","").replace("]","")
#
#         x = int(bounds_arr.split(",")[0])
#         y = int(bounds_arr.split(",")[2])
#
#         x_width = (int(bounds_arr.split(",")[2])-int(bounds_arr.split(",")[0]))/2
#         y_width = (int(bounds_arr.split(",")[3])-int(bounds_arr.split(",")[1]))/2
#
#         x_touch = int(x+x_width)
#         y_touch = int(y+y_width)
#
#         screen = {
#             "x":x,
#             "y":y
#         }
#
#         screen_taps.append(screen)
#
# for tap in screen_taps:
#     # print (tap)
#     popen("adb shell input tap {0} {1}".format(tap["x"],tap["y"]))
#     sleep(10)
#     popen("adb shell input keyevent {0}".format(4))
