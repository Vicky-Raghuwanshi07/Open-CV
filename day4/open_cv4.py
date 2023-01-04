########  DAY 4 ##########
import cv2
import numpy as np

width, height = 300, 50
img = cv2.imread('./car2.jpg')
# pts = np.array([[121,101], [171,101], [121,111],[176,111]])
# pts = np.array([[140,230], [230,230], [140,250],[230,250]])   #for car
pts = np.array([[328,635], [615,639], [330,683],[611, 687]])    #for car2
pts1 = np.array([[0,0], [width,0], [0,height], [width,height]])

for i in range(0,4):
    cv2.circle(img,(pts[i][0], pts[i][1]) , 5 , (0,0,255), cv2.FILLED)

pts = np.float32([[328,635], [615,639], [330,683],[611, 687]])
pts1 = np.float32([[0,0], [width,0], [0,height], [width,height]])

matrix = cv2.getPerspectiveTransform(pts,pts1)
output = cv2.warpPerspective(img, matrix, (width,height))
img = cv2.resize(img, (512,512))
cv2.imshow("Car", img)
cv2.imshow("Plate", output)
cv2.waitKey(0)