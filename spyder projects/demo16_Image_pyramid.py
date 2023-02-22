# -*- coding: utf-8 -*-


#Image Pyramids in OPENCV
#image blending 
#there are two types of image Pyramid-
#1)Guassian Pyramid 2)Laplacian Pyramids

import cv2
import numpy as np

img1= cv2.imread("E:\data\dog1.jpg")
img1 = cv2.resize(img1,(700,700))

#Guassian Pyramid 1)function cv2.pyrUp() -cv2.pyr.Down()
'''
pd1=cv2.pyrDown(img1)
pd2 =cv2.pyrDown(pd1)

cv2.imshow("pd1",pd1)
cv2.imshow("pd2",pd2)
cv2.imshow("img1",img1)


'''

img1 = img1.copy()
data =[img1]
for i in range(4):
    img1 =cv2.pyrDown(img1)
    data.append(img1)
    cv2.imshow("res"+str(i),img1)




cv2.waitKey(0)
cv2.destroyAllWindows()

