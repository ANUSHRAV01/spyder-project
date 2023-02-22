# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:53:54 2023

@author: anush
"""
#image dtection
#image gradient
#laplacian Derivative-- It calculate laplace derivative
#https://github.com/askitlouder/Image-Processing-Tutorials

#it is use multi-stage algorithm to detect a edge#
# 5 steps in this 1)GUASS(noise reduction) 2)Gradient calculate
#3)non-max suppression 4)double threshold 5)edge tacking by hysteresis

import cv2
import numpy as np

'''#Load image into gray scale
img =cv2.imread(r"E:\data\building.jpg")
img =cv2.resize(img,(400,400))
img_gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#canny(img,thresh1,thresh2)
canny =cv2.Canny(img_gray,50,150)

cv2.imshow("original",img)
cv2.imshow("gray",img_gray)
cv2.imshow("canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()'''

img =cv2.imread(r"E:\data\building.jpg")
img =cv2.resize(img,(400,400))
img_gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold","Canny",0,255,nothing)

while True:
    a=cv2.getTrackbarPos("Threshold","Canny")
    print(a)
    res = cv2.Canny(img_gray,a,255)
    cv2.imshow("canny1",res)
    K =cv2.waitKey(1)
    if K==27:
        break
cv2.destroyAllWindows()
        
    

