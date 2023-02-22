# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 10:07:49 2023

@author: anush
"""
import cv2
import numpy as np

img1=cv2.imread("E:\data\dog1.jpg")
img2=cv2.imread("E:\data\cat1.jpg")

img1 = cv2.resize(img1,(300,400))
img2 = cv2.resize(img2,(300,400))
#cv2.imshow("dog",img1)
#cv2.imshow("cat",img2)

def blend(x):
    pass

img =np.zeros((400,400,3),np.uint8)
cv2.namedWindow("win")#create a track bar
cv2.createTrackbar("alpha","win",1,100,blend)

switch = "0 :OFF \n 1:ON"
cv2.createTrackbar(switch,"win",0,1,blend)

while True:
    s =cv2.getTrackbarPos(switch,"win")
    a =cv2.getTrackbarPos("alpha","win")
    n=float(a/100)
    print(n)
    
    if s==0:
        dst =img[:]
    else:
        dst =cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(dst,str(a),(20,60),cv2.FONT_ITALIC,
                    2,(0,125,255),2)
    cv2.imshow("dst",dst)
    k=cv2.waitKey(1)
    if k==27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
