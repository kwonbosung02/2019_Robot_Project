import cv2
import numpy as np
import math

cam = cv2.VideoCapture(0)

while(cam.isOpened()):
    ret , img = cam.read()

    cv2.rectangle(img, (600,600), (100,100), (0,255,0),0)
    crop_img = img[100:600,100:600]

    grey = cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)

    gaussianBlurred = cv2.GaussianBlur(grey,(35, 35),0)
    
    #THRESH_BINARY_INV -> 반전
    #THRESH_OTSU -> 임계값 자동으로 계산 
    _, thresh1 = cv2.threshold(gaussianBlurred,157,235,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    cv2.imshow('test1',thresh1)
    cv2.imshow('test2',grey)
    end_out_key = cv2.waitKey(1)
    if end_out_key == 27:
        break