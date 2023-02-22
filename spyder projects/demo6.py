# -*- coding: utf-8 -*-

import cv2

img = cv2.imread(r"E:\data\aunt1.jpg",1)
print("shape==",img.shape)
print("size of== ",img.size)
print("datatype==",img.dtype)
print("imagetype==:",type(img))

#now we are going to split the array
img =cv2.resize(img,(400,500))
b,g,r= cv2.split(img)


'''cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.imshow("original",img)'''

s =cv2.merge((r,g,b))
cv2.imshow("rgb",s)

s =cv2.merge((r,g,b))
cv2.imshow("gb",s)
cv2.imshow("orginal",img)






cv2.imshow("res",img)

cv2.waitKey(0)
cv2.destroyAllWindows()