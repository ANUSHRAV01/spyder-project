# -*- coding: utf-8 -*-

import cv2 

img1 =cv2.imread("E:\\data\\cat1.jpg",1)
img1 =cv2.resize(img1,(300,290))#width,height
print(img1)
cv2.imshow("original",img1)

img2=cv2.imread("E:\\data\\cat1.jpg",0)
img2 =cv2.resize(img2,(300,270))
print(img2)
cv2.imshow("grey image",img2)

cv2.waitKey()
cv2.destroyAllWindows()