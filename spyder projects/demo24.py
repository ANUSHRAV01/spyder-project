# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:18:52 2023

@author: anush
"""
#optical Flow--Kanade method
#it is a pattern of apparent motion of image objects
#between two consecutive frames caused by th e movemnet

#pixels initensities of an object do not change  b/w consecutive frames


#face and eye detection in image

#face detection using haarcascade file
'''
import cv2
import numpy as np

img =cv2.imread(r"E:\data\a.jpg")
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face =cv2.CascadeClassifier("E:\data\cascades\haarcascade_frontalface_default.xml")

#parameters(img,scale_factor[reduce image size,min_neighbour])
faces =face.detectMultiScale(gray,1.4,4) #for faces

for(x,y,w,h) in faces:
    img =cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,205),3)

img =cv2.resize(img,(400,500))
cv2.imshow("face detected",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#face and eye detection using webcam
#HARCASCADE CLASSIFEIER TECHNIQUE

import cv2
import numpy
face=cv2.CascadeClassifier(r"E:\\Data\\cascades\\haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier(r'E:\\Data\\cascades\\haarcascade_eye.xml') #for detecting eyes
def dector(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,1.3,5)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,125),3)
        
        roi_gray = gray[y:y+h, x:x+w]
        
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye.detectMultiScale(roi_gray,1.3,3)
        for (ex,ey,ew,eh) in eyes:
            cv2.circle(roi_color,(ex+27,ey+27),20,(255,255,0),2)

    return img

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret,frame =cap.read()
    frame = cv2.flip(frame,2)
    cv2.imshow("face dect",dector(frame))
    if cv2.waitKey(1)==13:   # press enter to terminate
        break
    
cap.release()
cv2.destroyAllWindows()  



































