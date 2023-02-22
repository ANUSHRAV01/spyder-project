# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:35:38 2023

@author: anush
"""

#image smoothing or blurring

#it is used to remove noise from the image
#there are so many filter is use for smoothing the image
#there are Low Pass Filter(LPS) which use to remove Noise from the image

#we discuss about filters:-like,homogenous,blurr,guassian,median,bilateral


import cv2
import numpy as np

img1 =cv2.imread("E:\data\col_balls.jpg",0)
img1 =cv2.resize(img1,(200,300))
cv2.imshow("original",img1)

#rows and ccol and div by area(10,10-max(ht,w))
kernel=np.ones((5,5),np.float32)/25
#filter
h_filter = cv2.filter2D(img1,-1,kernel)
cv2.imshow("Homo",h_filter)

#blurr method

blur =cv2.blur(img1,(5,5))
cv2.imshow("blurr",blur)

#guassian methiod
#gau = cv2.GuassianBlur(img1,(5,5),0)#0 is sigma x which is clor based indicator
#cv2.imshow("gau",gau)


#bilateral filter will give the best method to do image smooth




cv2.waitKey(0)
cv2.destroyAllWindows()