# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:59:10 2023

@author: anush
"""
#Object Tracking using MeanShift Algo
#the idea behind this algo is to move small window to get the high
#density pixels same as histogram backprojection
#capshift,meanshift
#steps to use this algo---
#first setup target and find its histogram for backprooject the target
#also set one initial location
#setup the termination criteria

import cv2
import numpy as np
cap =cv2.VideoCapture("E:\data\test2.mp4")

#take first frame of the video
ret,frame =cap.read()

#setup initial location of windows
x,y,width,height =580,30,80,150
track =(x,y,width,height)

#setup the ROI for tracking
roi =frame[y:y+height,x:x+width]
hsv_roi =cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

mask =cv2.inRange(hsv_roi,np.array((0.,60.,32.))),
np.array((180.,255.,255))
roi_hist =cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)




while True:
    ret ,frame =cap.read()
    if ret == True:
        
        cv2.imshow("original",frame)
        
        k =cv2.waitKey(30)
        if k ==27:
            break
    else:
        break
cv2.destroyAllWindows()
