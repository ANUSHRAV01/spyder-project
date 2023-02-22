# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 16:09:39 2023

@author: anush
"""

import cv2
import numpy as np

def cross(x):
    pass

#blank
img = np.zeros((350,512,3), np.uint8)
cv2.namedWindow("Color Pickers")

#create switch 
s1= "0:OFF\n1:ON"
cv2.createTrackbar(s1,"Color Pickers",0,1,cross)

#creating for rgb

#Creating TrackBars for adjusting Colours
cv2.createTrackbar("R","Color Pickers",0,255,cross)
cv2.createTrackbar("G","Color Pickers",0,255,cross)
cv2.createTrackbar("B","Color Pickers",0,255,cross)

while True:
     cv2.imshow("Color Pickers",img)
     A =cv2.waitKey(1)
     if A==27:
         break
     #now get tracker position
     s = cv2.getTrackbarPos(s1,"Color Pickers")
     r = cv2.getTrackbarPos("R","Color Pickers")
     g = cv2.getTrackbarPos("G","Color Pickers")
     b = cv2.getTrackbarPos("B","Color Pickers")
     
     if s == 0:
         img[:] =0
     else:
        img[:] =[r,g,b]
cv2.destroyAllWindows()

     