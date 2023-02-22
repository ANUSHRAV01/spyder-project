# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:17:28 2023

@author: anush
"""

#Contours-Helps in shape detection,Analyzation and recognition

'''contours can be explained simply as a curve joining all the continuous points
having same color or intensity
for better accuracy,use binary images and also apply edge detection before #finding countours

find countours function maniplate original image so copy it before proceeding.
find countours is like finding white object from black background
so u must turn image in white and blackground in black

'''

import cv2
import numpy as np

img =cv2.imread("E:\data\logo.jpg")
img1 =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh =cv2.threshold(img1,20,255,0)#0 is bINARY METHOD number

#findcontour(img,countour_retrieval_mode,method)
cnts,hier =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(cnts,len(cnts))


#drawcontour(img,id of contour,color,thickness)
#contour just pass -1
#draw the contours

img =cv2.drawContours(img,cnts,-1,(15,200,15),4)

cv2.imshow("original==",img)
cv2.imshow("gray",img1)
cv2.imshow("thresh==",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
