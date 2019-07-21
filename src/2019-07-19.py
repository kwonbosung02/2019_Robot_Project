import cv2
import numpy as np

cam = cv2.VideoCapture(0)
def nothing(x):
    pass

if __name__ == "__main__":
    cv2.namedWindow('HSV_TrackBar')

    h, s, v = 100, 100, 100

    cv2.namedWindow('HSV_TrackBar')

    cv2.createTrackbar('h', 'HSV_TrackBar', 0, 179, nothing)
    cv2.createTrackbar('s', 'HSV_TrackBar', 0, 255, nothing)
    cv2.createTrackbar('v', 'HSV_TrackBar', 0, 255, nothing)

    lower_mask = np.array([2, 50, 50])
    upper_mask = np.array([15, 255, 255])

    while( True ):
        ret, frame = cam.read()
        blur = cv2.blur(frame,(3, 3))

        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        mask2 = cv2.inRange(hsv, lower_mask, upper_mask)
        #kernal_matrix
        #erosion 침식, dilation 팽창
    
        ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

        dilation = cv2.dilate(mask2, ellipse, 1)
        erosion = cv2.dilate(dilation, ellipse, 1)
        dilation2 = cv2.dilate(erosion, ellipse, 1)
        filtered = cv2.medianBlur(dilation2, 5)
        ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
        dilation2 = cv2.dilate(filtered, ellipse, 1)

        median = cv2.medianBlur(dilation2, 5)

        ret, thresh = cv2.threshold(median, 127,  255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            hull = cv2.convexHull(cnt)
            cv2.drawContours(blur, [hull], 0, (255, 0, 255), 5)

        cv2.imshow('blur', blur)

        cv2.imshow('dilation', dilation)
        cv2.imshow('erosion',erosion)
        cv2.imshow('dilation2', dilation2)

        cv2.imshow('filtered', filtered)


        end_out_key = cv2.waitKey(1) & 0xFF
        if end_out_key == 27:
            break

