# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:04:22 2023

@author: anush
"""

#corner Detection
#Harris Corner Detection

'''img -Input image it should be grayscale and float32 type.
blockSize -It is the size of neighbour considered for corner detection ksize-aperture parameter of sobel derivative used

'''
'''
import cv2
import numpy as np

img =cv2.imread(r"E:\data\shapes.png")
img =cv2.resize(img,(600,600))
#fray conversion
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray =np.float32(gray)
cv2.imshow("img",img)

#detect corner 
res =cv2.cornerHarris(gray,9,3,0.04)
res =cv2.dilate(res,None)
img[res >0.1*res.max()] =[0,0,255] #marked color


cv2.imshow("dst",img)
#cv2.imshow("img",img)
#cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#img[:,:]-means sara rows and sare col
#shi-Tomasi corner detector
#cv2.goodFeaturesToTrack().
#more efficive thab harris

import cv2
import numpy as np

img =cv2.imread("E:\data\shapes.png")
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#parameters(img,no.of corner,quality_level,min_distancebetween)
corners =cv2.goodFeaturesToTrack(gray,100,0.01,5)
corners =np.int64(corners)

for i in corners:
    x,y =i.ravel()#numpy-flatten the array(multi dimension array-linear dimension array)
    cv2.circle(img,(x,y),3,255,-1)
    
    
cv2.imshow("res==",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
