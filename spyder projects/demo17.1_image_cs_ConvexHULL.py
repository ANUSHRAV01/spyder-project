# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:35:03 2023

@author: anush
"""
#important topics here
#Contours and its functions
#Moments
#Approxiamation
#ConvexHull

import cv2
import numpy as np

img1 = cv2.imread("E:\data\shapes.png")
img1 = cv2.resize(img1,(600,700))
img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
_,thresh =cv2.threshold(img2,200,255,cv2.THRESH_BINARY_INV)

#FINDCONTOURS(img,contour_retrival_mode,method)
cnts,hier =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#Here cnts is list of contours
#hier variable called hierarchy and it contains image information
print("NUMBER OF CONTOURS",cnts,"\nTotal contours==",len(cnts))
print("Hierarchy==\n",hier)

#draw Contour:-
#img3 =cv2.drawContours(img1,cnts,-1,(10,20,100),2)#2 is the line sharpness or size can be increased
#loop over the contours
for c in cnts:
    #compute the center of the contours
    #an image moment is a certain particular weighted average(moment) of the image
    M =cv2.moments(c)
    print("M==",M)
    cX =int(M["m10"]/M["m00"])
    cY =int(M["m01"]/M["m00"])
    #draw the contours and center of the shape of the image
    #JAGAH,COLOR,THICKNESS IN DRAW
    cv2.drawContours(img1,[c],-1,(0,255,0),2)
    cv2.circle(img1,(cX,cY),7,(255,255,255),-1)
    #-(MINUS MEANING THAT IT IS GOING DOWNWARD DIRX)
    cv2.putText(img1,"center",(cX-20,cY-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(25,255,10),2)
    



cv2.imshow("thres",thresh)
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()




#contour ka area
#area = cv2.contourArea(c)
#area1.append(area)

#countour Approx -It is use to approx shape with less number of verticles
'''#0.1,0.005
epsilon = 0.1*cv2.arclength(c,True)#arc length take contour and return
data =cv2.approxPolyDP(c,epsilon,True)
#ConvexHull is used to provide proper contours convexity

hull =cv2.convexHull(data)

x,y,w,h =cv2.boundingRect(hull)
img =cv2.rectangle(img1,(x,y),(x+w,y+h),(125,10,20),5)


'''



