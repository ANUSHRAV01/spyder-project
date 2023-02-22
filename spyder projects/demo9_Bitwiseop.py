# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:19:09 2023

@author: anush
"""
#this is called masking(starting)
import cv2
import numpy as np

img1 =np.zeros((250,500,3),np.uint8)
img1 =cv2.rectangle(img1,(150,100),(200,250),(255,255,255),-1)


img2 =np.zeros((250,500,3),np.uint8)
img2 =cv2.rectangle(img2,(10,10),(170,60),(255,255,255),-1)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

bitAnd =cv2.bitwise_and(img2,img1)
cv2.imshow("bitAnd",bitAnd)

bitor =cv2.bitwise_or(img2,img1)
cv2.imshow("bitor",bitor)

#now try bitnot1, bitnot2,bitxor



cv2.waitKey(0)
cv2.destroyAllWindows()
