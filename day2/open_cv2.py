import cv2
import numpy as np


img = cv2.imread('mountain.jpg')
reshape = cv2.resize(img,(img.shape[1], img.shape[0]//2))
crop = img[250:img.shape[0], 300:450]
resize = cv2.resize(crop, (img.shape[1], img.shape[0]))
cv2.imshow("Mountain" , img)
print(img.shape)

cv2.imshow("Reshape Image" , reshape)
print(reshape.shape)

cv2.imshow("Mountain Croped" , crop)
print(crop.shape)
cv2.imshow("Mountain Resize" , resize)
print(crop.shape)

cv2.waitKey(0)