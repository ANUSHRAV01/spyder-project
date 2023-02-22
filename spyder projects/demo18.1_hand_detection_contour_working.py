# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:52:50 2023

@author: anush
"""
import cv2
import numpy as np

img = cv2.imread("E:/data/hand.jpg")
img = cv2.resize(img, (600, 700))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(img1, 9)
_, thresh = cv2.threshold(img1, 240, 255, cv2.THRESH_BINARY_INV)

# findContours(img,countour_retrival_mode,method)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Number of contours:", len(contours))

for c in contours:
    epsilon = 0.0001 * cv2.arcLength(c, True)
    data = cv2.approxPolyDP(c, epsilon, True)

    hull = cv2.convexHull(data)

    cv2.drawContours(img, [c], -1, (50, 50, 150), 2)
    cv2.drawContours(img, [hull], -1, (0, 255, 0), 2)

    # find convexity defect
    hull2 = cv2.convexHull(c, returnPoints=False)
    # defects returns an array which contains value [start_point,end_point,farthest_point,approx_point]
    defect = cv2.convexityDefects(c, hull2)

    if defect is not None:
        for i in range(defect.shape[0]):
            s, e, f, d = defect[i, 0]
            start = tuple(c[s][0])
            end = tuple(c[e][0])
            far = tuple(c[f][0])
            cv2.circle(img, far, 5, [0, 0, 255], -1)

cv2.imshow("original", img)
cv2.imshow("gray", img1)
cv2.imshow('thresh', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

