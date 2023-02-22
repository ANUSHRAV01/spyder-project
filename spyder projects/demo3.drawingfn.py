# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:29:31 2023

@author: anush
"""

#import numpy as np
import cv2

img =cv2.imread("E:\data\Cat1.jpg",1)
#gray =cv2.imread("E:\data\Cat1.jpg",0) 
gray = cv2.cvtColor(img,(cv2.COLOR_BGR2GRAY))

#img =np.zeros([512,512,3],np.uin8)*255 #for black screen
#img = np.ones([512,512,3], np.uint8)*255 for white screen on img

#here line covers 5 parameters (img,start,ending,clor,thick)
img=cv2.line(img,(0,0),(200,200),(50,40,250),9)

#here line covers 5 parameters (img,start,ending,clor,thick)
img=cv2.line(img,(0,0),(200,200),(255,0,149),9)

#here line covers 5 parameters (img,start,ending,clor,thick)
img=cv2.line(img,(0,0),(200,200),(50,40,250),9)

#here line covers 5 parameters (img,start,radius,clor,thick)
img=cv2.circle(img,(200,200),50,(50,230,250),-1)

font=cv2.FONT_ITALIC
#parameters are #putText -accept()(img,text,start_co,fontsize,color,thickness,linetype)
img=cv2.putText(img,"sweet cat",(70,100),font,4,(0,125,125),10,cv2.LINE_AA)

#for ellipse para-(img,start_co,(length,height),clor,thickness)
img =cv2.ellipse(img,(250,450),(100,50),0,0,270,125,5)

cv2.imshow("gray",gray)
cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



