import cv2
import numpy as np

def empty(a):
    pass

frameWidth = 500
frameHeight = 340

# url = "https://192.168.1.32:8080/video"
# cap = cv2.VideoCapture(0)
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("Hue Min", "HSV", 0, 179, empty)
cv2.createTrackbar("Hue Max","HSV",179,179,empty)
cv2.createTrackbar("Sat Min","HSV",0,255,empty)
cv2.createTrackbar("Sat Max","HSV",255,255,empty)
cv2.createTrackbar("Val Min","HSV",0,255,empty)
cv2.createTrackbar("Val Max","HSV",255,255,empty)

while True:
    # _, img = cap.read()
    img = cv2.imread('./balls.jpeg')
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("Hue Min", "HSV")
    h_max = cv2.getTrackbarPos("Hue Max", "HSV")
    s_min = cv2.getTrackbarPos("Sat Min", "HSV")
    s_max = cv2.getTrackbarPos("Sat Max", "HSV")
    v_min = cv2.getTrackbarPos("Val Min", "HSV")
    v_max = cv2.getTrackbarPos("Val Max", "HSV")
    
    lower = np.array([h_min,s_min, v_min])
    upper = np.array([h_max,s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img,result])
    
    # cv2.imshow("Original", img)
    # cv2.imshow("HSV", imgHSV)
    # cv2.imshow("MASK", mask)
    # cv2.imshow("Result", result)
    cv2.imshow('stack', hstack)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()