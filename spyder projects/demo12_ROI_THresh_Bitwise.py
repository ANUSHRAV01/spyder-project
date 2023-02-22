# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:22:56 2023

@author: anush
"""

import cv2
import numpy as np

img1 = cv2.imread("E:\data\hero1.jpg")
img2 =cv2.imread("E:\data\\strom_breaker.jpg")

img1 = cv2.resize(img1,(1024,650))
img2 = cv2.resize(img2,(600,650))

#fix image 2 data into img1
r,c,ch =img2.shape
print(r,c,ch)

#roi ==
roi = img1[0:r,0:c]

#Now creating mask for img2
img_gry =cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#create mask using threshold
_,mask =cv2.threshold(img_gry,45,255,cv2.THRESH_BINARY)


#remove bg
mask_inv =cv2.bitwise_not(mask)

#put mask into roi
img1_bg =cv2.bitwise_and(roi,roi,mask=mask_inv)


#take only region of figure from original image
img2_fg = cv2.bitwise_and(img2,img2,mask =mask)

# put img in ROI and modify the main image
res =cv2.add(img1_bg,img2_fg)



#cv2.imshow("THor",img1)
#cv2.imshow("Storm_breaker",img2)
#cv2.imshow("roi__",roi)
#cv2.imshow("storm1",img_gry)
#cv2.imshow("mask",mask)
cv2.imshow("mask-inv3",mask_inv)
cv2.imshow("mask-next5",img2_fg)
cv2.imshow("step6",res)

final = img1

final[0:r,0:c] =res
cv2.imshow("step 7==Final",final)


cv2.waitKey(0)
cv2.destroyAllWindows()

