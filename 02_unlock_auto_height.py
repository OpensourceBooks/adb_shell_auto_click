from os import popen
from time import sleep

size=popen("adb shell wm size").read().split(" ")[2]
w = size.split("x")[0]#手机像素的宽度
h = size.split("x")[1]#手机像素的高度，也就是用于从下到上滑动的底部

touch_w=int(w)/2
touch_h=int(h)-50

popen("adb shell input keyevent 82")
sleep(1)
popen("adb shell input swipe {0} {1} {0} 0 800".format(touch_w,touch_h))
