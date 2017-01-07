import cv2 
import os 
import numpy as np 


def BlueFilter(frame): 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    
    boundary = [np.array([115,128,128]), np.array([130, 256, 256])]
    mask = cv2.inRange(hsv_frame, boundary[0], boundary[1]) 
    res = cv2.bitwise_and(hsv_frame, hsv_frame, mask = mask) 
    output = cv2.cvtColor(res, cv2.COLOR_HSV2BGR) 
    return output

def StartCamera(): 
    webcam = cv2.VideoCapture(0) 
    
    ret, frame = webcam.read()  
    while(ret): 
        cv2.namedWindow("BlueTest") 
        cv2.namedWindow("RedTest") 
        blueFrame = BlueFilter(frame) 
        cv2.imshow("BlueTest", blueFrame) 
        cv2.imshow("RedTest", frame) 
        ret, frame = webcam.read()  
        if (cv2.waitKey(20) & 0xFF == 27): 
            break 
    cv2.destroyAllWindows()

StartCamera() 
