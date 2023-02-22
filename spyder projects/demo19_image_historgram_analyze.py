# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:56:00 2023

@author: anush
"""

#Image Histogram -Find ,Plot and Analyze
#it which gives u an overall idea about the intensity distribution of  an image
#it distribute data along x and y axis
#x -axis contains range of color values
#y -axis contain numbers of pixels in an image
#with histogram to extract information about contact,brightness and intensity etc,
#plot histogram using matplotlib

import cv2
import numpy as np
from matplotlib import pyplot as plt

#plotting with calhist method

img =np.zeros((200,200),np.uint8)
cv2.rectangle(img,(0,100),(200,200),(255),-1)
cv2.rectangle(img,(0,50),(50,100),(127),-1)
#it accept parameters like[img],[channel],mask,[histsize],range[0-255]
hist =cv2.calcHist([img],[0],None,[256],[0,256])


plt.plot(hist)
plt.show()
cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
img =cv2.imread(r"E:\data\aunt1.jpg")
img =cv2.resize(img,(400,400))
img_gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equ =cv2.equalizeHist(img_gray)
res =np.hstack((img_gray),equ)#stacking images side-by-side
cv2.imshow("equ",res)
hist1 =cv2.calcHist([equ],[0],None,[256],[0,256])
plt.plot(hist1)
plt.tille("Equalization")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
contrast limited adaptive Histogram Equalization
'''
