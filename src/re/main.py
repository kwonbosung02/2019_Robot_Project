
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0,"../functions/detect_cv2.py")
sys.path.insert(0,"../functions/const.py")
from functions import detect_cv2 as d
from functions import const as c
import cv2
import numpy as np
import copy
import serial
ser = serial.Serial('COM4', 9600)


camera = cv2.VideoCapture(0)
camera.set(10,200)
cv2.namedWindow('trackbar')
cv2.createTrackbar('thr1', 'trackbar', c.threshold, 100, d.print_threshold)

if __name__ == "__main__":
    counter = 0
    while camera.isOpened():
        ret, frame = camera.read()

        threshold = cv2.getTrackbarPos('thr1', 'trackbar')
        frame = cv2.bilateralFilter(frame, 5, 50, 100)
        frame = cv2.flip(frame, 1)
        cv2.rectangle(frame, (int(c.cap_region_x_begin * frame.shape[1]), 50),  (frame.shape[1], int(c.cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)
        cv2.imshow('original', frame)

        if c.is_background_captured == 1:
            img = d.remove_background(frame)
            img = img[50:int(c.cap_region_y_end * frame.shape[0]), int(c.cap_region_x_begin * frame.shape[1]):frame.shape[1]]

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (c.blurValue, c.blurValue), 0)
            ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)
            thresh1 = copy.deepcopy(thresh)
            try:
                contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            except:
                print("error")

            length = len(contours)
            maxArea = -1

            if length > 0:
                for i in range(length):
                    tem = contours[i]

                    c.area = cv2.contourArea(tem)
                    if c.area > maxArea:
                        maxArea = c.area
                        c_i = i
                for cnt in contours:
                    try:
                        M = cv2.moments(cnt)
                        global cx, cy
                        cx = int(M['m10'] / M['m00'])
                        cy = int(M['m01'] / M['m00'])
                    except:
                        pass
                cv2.setMouseCallback('draw_obj', d.CallBackFunction)
                res = contours[c_i]
                hull = cv2.convexHull(res)
                compare = (cx,cy)
                print(d.return_compare(compare))
                draw_Object = np.zeros(img.shape, np.uint8)
                cv2.drawContours(draw_Object, [res], 0, (0, 255, 0), 2)
                cv2.drawContours(draw_Object, [hull], 0, (255, 255, 0), 2)
                cv2.circle(draw_Object, (cx, cy), 10, (0, 0, 255), -1)
                MAX_y = draw_Object.shape[0]
                MAX_x = draw_Object.shape[1]
                d.draw____(draw_Object,MAX_x,MAX_y)

                calc, cnt = d.calculate(res, draw_Object)
                if c.trigger_switch == True:
                    try:
                        if counter % 10 == 0:
                            ser.write(str(cnt).encode('utf-8'))
                            print("============SENDED============")
                    except:
                        print("==============ERR==============")

                    '''print(cnt)'''

            cv2.imshow('masked', img)
            cv2.imshow('blur', blur)
            cv2.imshow('threshold', thresh)
            cv2.imshow('draw_obj', draw_Object)
        ########
        counter = counter + 1
        print(counter)
        k = cv2.waitKey(1)

        if k == 27:  # press ESC to exit
            camera.release()
            cv2.destroyAllWindows()
            break
        elif k == ord('b'):
            d.bgModel = cv2.createBackgroundSubtractorMOG2(0, c.background_Subtract_Threshold)
            c.is_background_captured = 1
            '''print("capured")'''

        elif k == ord('r'):
            d.bgModel = None
            c.trigger_switch = False
            is_background_captured = 0
            '''print('reset')'''
        elif k == ord('k'):
            c.trigger_switch = True
            print("================ Trigger ON ================")
        elif k == ord('o'):
            c.trigger_switch = False
            print("================ Trigger OFF ================")