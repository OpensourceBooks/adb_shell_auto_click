from os import popen

#手机像素的高度，也就是用于从下到上滑动的底部
h=800

popen("adb shell input keyevent 82")
popen("adb shell input swipe 50 {0} 50 0 500".format(800))
