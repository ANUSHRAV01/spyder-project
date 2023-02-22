# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:49:53 2023

@author: anush
"""
#Adaptive thresholding
#simple thresholding-either high or low 
#this one is good for the low luminous pixels
#this, the algorithm calculate the threshold for a small regions of the image.
#so,we get multiple threshold for diff.regions in same image.

#Adaptive Method -it calculates how threshoding value is calculated
#cv2.ADAPTIVE_THRESH_MEAN_C:
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C:
    
#THRESHOLD(img,pixel_thresh,max_thresh_pixel,method,style,no.of pixels,contact_mean)

import cv2
import numpy as np

img1 = cv2.imread("E:\data\page.jpg",0)
img1 = cv2.resize(img1,(400,400))
_, th1 =cv2.threshold(img1,127,255,cv2.THRESH_BINARY)

th2 =cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 =cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


cv2.imshow("Image",img1)
cv2.imshow("THRESH_BINARY", th1)
cv2.imshow("Adaptive_thresholding",th2)
cv2.imshow("guassian",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()