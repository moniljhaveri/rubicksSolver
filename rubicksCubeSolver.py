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

def WhiteFilter(frame): 
    hsl_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    
    boundary = [np.array([200, 0, 60]), np.array([220, 255, 255])]
    mask = cv2.inRange(frame, boundary[0], boundary[1]) 
    res = cv2.bitwise_and(hsl_frame, hsl_frame, mask = mask) 
    output = cv2.cvtColor(res, cv2.COLOR_HSV2BGR) 
    return output 

def OrangeFilter(frame): 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    
    boundaryL = [np.array([10, 100, 50]), np.array([20, 256, 256])]
    #boundaryU = [np.array([160, 128, 128]), np.array([179, 256, 256])]
    mask0 = cv2.inRange(hsv_frame, boundaryL[0], boundaryL[1]) 
    #mask1 = cv2.inRange(hsv_frame, boundaryU[0], boundaryU[1]) 
    mask = mask0# + mask1
    res = cv2.bitwise_and(hsv_frame, hsv_frame, mask = mask) 
    output = cv2.cvtColor(res, cv2.COLOR_HSV2BGR) 
    return output

def RedFilter(frame): 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    
    #boundaryL = [np.array([0, 128, 128]), np.array([10, 256, 256])]
    boundaryU = [np.array([160, 128, 128]), np.array([180, 256, 256])]
    #mask0 = cv2.inRange(hsv_frame, boundaryL[0], boundaryL[1]) 
    mask1 = cv2.inRange(hsv_frame, boundaryU[0], boundaryU[1]) 
    mask = mask1# + mask1
    res = cv2.bitwise_and(hsv_frame, hsv_frame, mask = mask) 
    output = cv2.cvtColor(res, cv2.COLOR_HSV2BGR) 
    return output

def StartCamera(): 
    webcam = cv2.VideoCapture(0) 
    
    ret, frame = webcam.read()  
    while(ret): 
        cv2.namedWindow("NamedWindow") 
        cv2.namedWindow("BlueTest") 
        cv2.namedWindow("OrangeTest") 
        cv2.namedWindow("RedTest") 
        cv2.namedWindow("WhiteTest") 

        blueFrame = BlueFilter(frame) 
        orangeFrame = OrangeFilter(frame) 
        redFrame = RedFilter(frame)
        whiteFrame = WhiteFilter(frame)

        cv2.imshow("NamedWindow", frame) 
        cv2.imshow("WhiteTest", whiteFrame) 
        cv2.imshow("BlueTest", blueFrame) 
        cv2.imshow("OrangeTest", orangeFrame) 
        cv2.imshow("RedTest", redFrame) 

        ret, frame = webcam.read()  

        if (cv2.waitKey(20) & 0xFF == 27): 
            break 
    cv2.destroyAllWindows()

StartCamera() 
