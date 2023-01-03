import cv2
import numpy as np


img = np.ones((512,512,3), np.uint8)
cv2.line(img, (0,0), (img.shape[1],img.shape[1]), (255,0,0), 1)

cv2.rectangle(img, (450,50), (300,100), (0,0,255), cv2.FILLED)
cv2.rectangle(img, (450,300), (350,250), (0,255,255), 2)
cv2.circle(img, (100,400), 80, (0,255,0), cv2.FILLED)
cv2.circle(img, (100,250), 30, (255,255,0), 2)

cv2.putText(img, "#Day3", (180,30), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,0,0), 2)

cv2.line(img, (300,40), (160,40), (255,0,0), 1)
cv2.imshow("Different Shapes",img)
cv2.waitKey(0)