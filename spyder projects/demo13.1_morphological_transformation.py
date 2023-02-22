# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:53:38 2023

@author: anush
"""

import cv2
import numpy as np

#opening
#first erosion anss then dilution


img1 = cv2.imread("E:\data\col_balls.jpg")
_,mask =cv2.threshold(img1,230,255,cv2.THRESH_BINARY_INV)
kernel =np.ones((4,4),np.uint8)
o =cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
cv2.imshow("opening",o)

c=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
cv2.imshow("closing",c)

#open,close,tophat,gradient,blackhat

cv2.waitKey(0)
cv2.destroyAllWindows()