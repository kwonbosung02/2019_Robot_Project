
import cv2
import numpy as np
import copy
import math

cap_region_x_begin=0.5
cap_region_y_end=0.8
threshold = 60
blurValue = 41
background_Subtract_Threshold = 50
learningRate = 0

is_background_captured = 0
trigger_switch = False

camera = cv2.VideoCapture(0)
camera.set(10,200)

def print_threshold(self):
    print("threshold = " + str(self))
cv2.namedWindow('trackbar')
cv2.createTrackbar('trh1', 'trackbar', threshold, 100,print_threshold)

def remove_background(frame):
    fgmask = bgModel.apply(frame,learningRate=learningRate)
    kernel = np.ones((3,3),np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1) #이미지 침식
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res

if __name__ == "__main__":

    while camera.isOpened():
        ret, frame = camera.read()
        threshold = cv2.getTrackbarPos('thr1','trackbar')
        frame = cv2.bilateralFilter(frame, 5, 50, 100)
        frame = cv2.flip(frame, 1)

        cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),
                  (frame.shape[1], int(cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)
        cv2.imshow('original', frame)

        if is_background_captured == 1:
            img = remove_background(frame)
            img = img[0:int(cap_region_y_end * frame.shape[0]),
                  int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]

            cv2.imshow('masked', img)

            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (blurValue, blurValue), 0)
            cv2.imshow('blurred', blur)

        k = cv2.waitKey(10)

        if k == 27:  # press ESC to exit
            camera.release()
            cv2.destroyAllWindows()
            break
        elif k == ord('b'):
            bgModel = cv2.createBackgroundSubtractorMOG2(0, background_Subtract_Threshold)
            is_background_captured = 1
            print("capured")
