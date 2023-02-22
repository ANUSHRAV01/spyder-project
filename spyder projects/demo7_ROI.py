# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 18:59:21 2023

@author: anush
"""

import cv2
import numpy as np

#read
img = cv2.imread(r"E:\data\aunt1.jpg")
img = cv2.resize(img,(400,600))

#ROI(region of interest)
#(110,200)  #(239,321)
#[(y1:y2),(x1:x2)]
#find the diff and then apply that difference with the image
#look for coor in paint and then use wisely
img1= img[110:200,239:321]

img[110:200,322:410] =img1
img[110:200,322:410] =img1



cv2.imshow("img1",img1)
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()