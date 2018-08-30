import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("1.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.subplot(121),plt.imshow(gray,'gray')
plt.xticks([]),plt.yticks([])

circles1 = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,
600,param1=100,param2=30,minRadius=80,maxRadius=97)
circles = circles1[0,:,:]
circles = np.uint16(np.around(circles))
for i in circles[:]:
  cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),5)
  cv2.circle(img,(i[0],i[1]),2,(255,0,255),10)
  cv2.rectangle(img,(i[0]-i[2],i[1]+i[2]),(i[0]+i[2],i[1]-i[2]),(255,255,0),5)

print("圆心坐标",i[0],i[1])
plt.subplot(122),plt.imshow(img)
plt.xticks([]),plt.yticks([]) 
