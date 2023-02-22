# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:08:51 2023

@author: anush
"""

#Hough transform

#convert image into gray
#detect edges
#then apply hough method

#houghLines-help of lines 
#cartesian CS(y=mx+c) and polar cs->xcoso +ysinO


import cv2
import numpy as np


img = cv2.imread("E:\data\chess.jpg")
img =cv2.resize(img,(400,400))
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges =cv2.Canny(gray,20,250)


#function accept parameters(img,rho,theta)
#lines =cv2.HoughLines(edges,1,np.pi/180,200)
#rho value-distance resolution of pixels

lines =cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=8,maxLineGap=100)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(100,200,125),2)
#thetha -angle resolution
#line threshold
'''
for rho,theta in lines[0]:
    a =np.cos(theta)
    b=np.sin(theta)
    x0 =a*rho
    y0 =b*rho
    x1 =int(x0 + 1000*(-b))
    y1 =int(y0 +1000*(a))
    x2 =int(x0 -1000*(-b))
    y2 =int(y0 -1000*(a))
    
    cv2.line(img,(x1,y1),(x2,y2),(255,0,255),2)
    '''
cv2.imshow("edges",edges)
cv2.imshow("lines",img)


cv2.waitKey(0)
cv2.destroyAllWindows()