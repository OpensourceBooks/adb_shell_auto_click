from os import popen
from time import sleep
from time import time

filename = str(int(time()))
#把当前的屏幕控件保存到手机的sd卡
popen("adb shell uiautomator dump /sdcard/{0}.xml".format(filename))

#延时5秒钟，确保xml已经保持
sleep(5)

#把xml文件保存在项目的temp_ui目录
popen("adb pull /sdcard/{0}.xml temp_ui".format(filename))


#popen("adb shell input swipe {0} {1} {0} 0 800".format(touch_w,touch_h))
