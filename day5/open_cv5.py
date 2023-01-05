########  DAY 5 ##########
import cv2
import numpy as np
points = np.zeros((4,2) )
counter = 0
def mouseClick(event, x,y, flag, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        points[counter] = x,y
        counter+=1
        print(x,y)
        
img = cv2.imread('./car3.jpg')
img = cv2.resize(img, (800,512))
cv2.imshow("img", img)
while True:
    width, height = 300, 50
    if counter==4:
        pts = np.float32([points[0], points[1], points[2],points[3]])
        pts1 = np.float32([[0,0], [width,0], [0,height], [width,height]])
        matrix = cv2.getPerspectiveTransform(pts,pts1)
        output = cv2.warpPerspective(img, matrix, (width,height))
        cv2.imshow("Plate", output)
        cv2.waitKey(0)
    elif counter<4:
        cv2.setMouseCallback("img", mouseClick)
    else:
        break
    cv2.waitKey(1)
# cv2.waitKey(1)