# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:48:33 2023

@author: anush
"""

import cv2

cap=cv2.VideoCapture(r"E:\data\sd.mp4")
print("cap",cap)

while True:
    ret,frame =cap.read()
    frame = cv2.resize(frame,(500,450))
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    cv2.imshow("frame",frame)
    k = cv2.waitKey(25)
    if k == ord("s"):
        break
cap.release()
cv2.destroyAllWindows()


#now capture video from webcam
'cap=cv2.VideoCapture(0)'

#divx,xvid,mjeg,x264,WMV1,WMV2
fourcc =cv2.VideoWriter_fourccc(*"XVID")
#4para,name,codec,fps,resoution
'''output =cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))

print(cap)

while cap.isOpened():
    ret,frame =cap.read()
    if ret == True:
        frame = cv2.resize(frame,(500,450))
        gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray",gray)
        cv2.imshow("frame",frame)
        k = cv2.waitKey(25)
        if k == ord("s") :
            break
cap.release()
cv2.destroyAllWindows()'''



