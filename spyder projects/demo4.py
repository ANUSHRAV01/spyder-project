# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 12:30:22 2023

@author: anush
"""

import cv2
import numpy as np

def draw(event,x,y,flag,param):
    if event ==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(125,0,255),5)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img,(x,y),(x+100,y+75),(125,125,255),2)
        
cv2.namedWindow(winname ="res")

img = np.zeros((512,512,3), np.uint8)
cv2.setMouseCallback("res",draw)

while True:
    cv2.imshow("res",img)
    A = cv2.waitKey(1)
    if A ==ord("q"):
        break   #esc
        
cv2.destroyAllWindows()