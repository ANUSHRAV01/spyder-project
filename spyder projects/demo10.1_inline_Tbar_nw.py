# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:39:34 2023

@author: anush
"""

import cv2
import numpy as np

img1 =cv2.imread("E:\data\color_balls.jpg")
img1 =cv2.resize(img1,(600,400))



def nothing(x):
    pass
cv2.namedWindow("Color Adjustments")


cv2.createTrackbar("Lower_H","Color Adjustments",0,255,nothing) 
cv2.createTrackbar("Lower_S","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_V","Color Adjustments",0,255,nothing)
 #NAME,TYPE,INITIAL ,FINAL
cv2.createTrackebar("Upper_H","Color Adjustments",255,255,nothing)
cv2.createTrackbar("Upper_S","Color Adjustments",255,255,nothing)
cv2.createTrackbar("Upper_V","Color Adjustments",255,255,nothing)

#now we need to bound them together   

while True:
    hsv =cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
    
    l_h =cv2.getTrackbarPos("Lower_H","Color Adjustments")
    l_s =cv2.getTrackbarPos("Lower_S","Color Adjustments")
    l_v =cv2.getTrackbarPos("Lower_V","Color Adjustments")
    
    u_h =cv2.getTrackbarPos("Upper_H","Color Adjustments")
    u_s =cv2.getTrackbarPos("Upper_S","Color Adjustments")
    u_v =cv2.getTrackbarPos("Upper_V","Color Adjustments")
    
    
    lower_bound = np.array([l_h,l_s,l_v])
    upper_bound = np.array([u_h,u_s,u_v])
    
    mask = cv2.inRange(hsv,lower_bound,upper_bound)
    
    #filter mask with image
    res = cv2.bitwise_and(img1,img1,mask=mask)
    
    cv2.imshow("original frame",img1)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    
    A = cv2.waitKey(1)
    if A == 27:
        break
    
cv2.destroyAllWindows()
    
    
    