import cv2 
import os 
import numpy as np 

def startCamera(): 
    webcam = cv2.VideoCapture(0) 
    
    ret, frame = webcam.read()  
    while(ret): 
        cv2.namedWindow("BlueTest") 
        cv2.imshow("BlueTest", frame) 
        ret, frame = webcam.read()  
        if (cv2.waitKey(20) & 0xFF == 27): 
            break 
    cv2.destroyAllWindows()

startCamera() 
