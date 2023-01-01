import cv2
import numpy as np


# kernel = np.ones((5,5),np.uint8)

# img = cv2.imread('./virat.jpg')
# Grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blurimg = cv2.GaussianBlur(Grayimg, (11,11),0)
# Canny = cv2.Canny(Blurimg, 50,90)
# deilation = cv2.dilate(Canny, kernel=kernel, iterations=1)
# un_deilate = cv2.erode(deilation, kernel=kernel, iterations=1)
# cv2.imshow("Read Image",img)
# cv2.imshow("Color To Grey Scale",Grayimg)
# cv2.imshow("Blur Image",Blurimg)
# cv2.imshow("Canny Effect",Canny)
# cv2.imshow("Dilate Image",deilation)
# cv2.imshow("Erode Image",un_deilate)
# cv2.waitKey(0)






url = "http://192.168.1.32:8080/video"
cap = cv2.VideoCapture(url,)
while(True):
    camera, frame = cap.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()