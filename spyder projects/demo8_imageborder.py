# -*- coding: utf-8 -*-

import cv2
import numpy as np

img1= cv2.imread(r"E:\data\dog1.jpg")
img1 =cv2.resize(img1,(400,500))


#creating i mage border
#parameters(img,border_width(4-sides),bordertype,val_border)
#top,bottom,right,left
img1= cv2.copyMakeBorder(img1,10,10,15,15,cv2.BORDER_CONSTANT,value=[255,0,125])



cv2.imshow("res",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

