# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:33:18 2023

@author: anush
"""

#thresholding
#3 types -simple,adaptive
#simple threshold(img,pixel_thresh,max_thresh,style)

import cv2
import numpy as np

img1 = cv2.imread("E:\\data\\black_white.png")
img1 = cv2.resize(img1,(300,200))

_, th1 =cv2.threshold(img1,50,255,cv2.THRESH_BINARY)
_, th2 =cv2.threshold(img1,50,255,cv2.THRESH_BINARY_INV)
_, th3 =cv2.threshold(img1,127,255,cv2.THRESH_TRUNC)
_, th4 =cv2.threshold(img1,127,255,cv2.THRESH_TOZERO)
_, th5 =cv2.threshold(img1,127,255,cv2.THRESH_TOZERO_INV)



cv2.imshow("1-THRESH_BINARY",th1)
cv2.imshow("2-THRESH_BINARY",th2)
cv2.imshow("3-THRESH_BINARY",th3)
cv2.imshow("4-THRESH_BINARY",th4)
cv2.imshow("5-THRESH_BINARY",th5)

cv2.imshow("original",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
