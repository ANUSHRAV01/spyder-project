# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:48:07 2023

@author: anush
"""

#HSV(huge saturation value)

import cv2
import numpy as np

img1 = cv2.imread('E:\data\color_balls.jpg')


while True:
    hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
    u_v = np.array([130,235,225])#most luminous
    l_v = np.array([110,50,50])#least luminious
    
    #create a mask it will filter other variables
    mask =cv2.inRange(hsv,l_v,u_v)
    
    #filter mask
    res =cv2.bitwise_and(img1,img1,mask=mask)
    
    cv2.imshow("img1",img1)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    
    A = cv2.waitKey(1)
    if A == 27:
        break
cv2.destroyAllWindows()
    