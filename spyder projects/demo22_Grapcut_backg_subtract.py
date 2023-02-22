# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:41:54 2023

@author: anush
"""


#grapcut algo cutoff any forground object from image or video
#it works like a reactangle portion on the image
#

import cv2
import numpy as np

img1 = cv2.imshow("E:\data\car.jpg")
img1 = cv2.resize(img1,(800,800))

mask = np.zeros(img1.shape[:2],np.uint8)

bgdModel =np.zeros((1,65),np.float64)*225

fgdModel =np.zeros((1,65),np.float64)*225






