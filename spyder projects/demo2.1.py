# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:01:04 2023

@author: anush
"""

import cv2
import datetime

'''cap=cv2.VideoCapture(r"E:\data\sd.mp4")
print("cap",cap)

while True:
    ret,frame=cap.read()
    frame =cv2.resize(frame,(300,160)) 
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    cv2.imshow("frame",frame)
    A = cv2.waitKey(100)
    if A == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()'''


cap=cv2.VideoCapture(0)
print(cap)

while cap.isOpened():
    ret,frame=cap.read()
    if ret == True:
        frame =cv2.resize(frame,(600,460)) 
        font =cv2.FONT_HERSHEY_COMPLEX_SMALL
        #this is for writting the text and height and width
        text ="height:" +str(cap.get(4)) +"width:" +str(cap.get(3))
        frame =cv2.putText(frame,text,(10,20),font,1,(0,155,255),1,cv2.LINE_AA)
        
        #this is for the date and time
        date_data ="DATE:" +str(datetime.datetime.now())
        frame =cv2.putText(frame,date_data,(20,50),font,1,(100,5,255),1,cv2.LINE_AA)        
        #we can make module and print here
        gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray",gray)
        cv2.imshow("frame",frame)
        A = cv2.waitKey(100)
        if A == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()



