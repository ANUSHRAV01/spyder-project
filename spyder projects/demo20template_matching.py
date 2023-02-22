# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:44:29 2023

@author: anush
"""

import cv2
import numpy as np

#target
img =cv2.imread(r"E:\data\avengers1.jpg")
grey_img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#load template
template =cv2.imread(r"E:\data\temp.jpg",0)
w ,h =template.shape[::-1]

#template matching
#this function accept parameters(img,template,method)
res =cv2.matchTemplate(grey_img,template,cv2.TM_CCORR_NORMED)
print("res==",res)

threshold =0.98
#loc is used to crop the fig
loc =np.where(res >=threshold)
count =0
for i in zip(*loc[::-1]):
    print("i==",i)
    cv2.rectangle(img,i,(i[0]+w,i[1]+h),(0,0,255),2)
    count +=1
    
    
img =cv2.resize(img,(800,600))
cv2.imshow("img",img)
print(count)
img =cv2.resize(img,(800,600))
#cv2.imshow("match temp==",res)
cv2.waitKey(0)
cv2.destroyAllWindows()