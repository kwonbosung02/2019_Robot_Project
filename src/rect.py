
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


def remove_background(frame):
    fgmask = bgModel.apply(frame,learningRate=learningRate)
    kernel = np.ones((3,3),np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1) #이미지 침식
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res

def calculate(res, drawing):
    hull = cv2.convexHull(res, returnPoints=False)
    if len(hull) > 3:
        defects = cv2.convexityDefects(res, hull)
        if type(defects) != type(None):

            cnt = 0

            for i in range(defects.shape[0]):
                start, end, far, defect = defects[i][0]
                start__ = tuple(res[start][0])
                end__ = tuple(res[end][0])
                far__ = tuple(res[far][0])

                a = math.sqrt((end__[0] - start__[0]) ** 2 + (end__[1] - start__[1]) ** 2)
                b = math.sqrt((far__[0] - start__[0]) ** 2 + (far__[1] - start__[1]) ** 2)
                c = math.sqrt((end__[0] - far__[0]) ** 2 + (end__[1] - far__[1]) ** 2)

                angle = math.acos((b ** 2 + c ** 2 - a ** 2)/(2 * b * c))
                if angle < math.pi / 2:
                    cnt += 1
                    cv2.circle(drawing, far__, 8, [211, 84, 0], -1)
                    cv2.circle(drawing, end__, 8, [0, 211, 0], -1)
            return True, cnt
        return False, 0



cv2.namedWindow('trackbar')
cv2.createTrackbar('thr1', 'trackbar', threshold, 100, print_threshold)


if __name__ == "__main__":

    while camera.isOpened():
        ret, frame = camera.read()
        threshold = cv2.getTrackbarPos('thr1', 'trackbar')
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

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (blurValue, blurValue), 0)
            cv2.imshow('blur', blur)
            ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)

            cv2.imshow('threshold', thresh)

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

                    area = cv2.contourArea(tem)

                    if area > maxArea:
                        maxArea = area
                        c_i = i
                for cnt in contours:
                    try:
                        M = cv2.moments(cnt)

                        cx = int(M['m10'] / M['m00'])
                        cy = int(M['m01'] / M['m00'])
                    except:
                        pass
                res = contours[c_i]
                hull = cv2.convexHull(res)
                draw_Object = np.zeros(img.shape, np.uint8)

                cv2.drawContours(draw_Object, [res], 0, (0, 255, 0), 2)
                cv2.drawContours(draw_Object, [hull], 0, (255, 255, 0), 2)
                cv2.circle(draw_Object, (cx, cy), 10, (0, 0, 255), -1)

                calc, cnt = calculate(res, draw_Object)
                if trigger_switch == True:
                    print(cnt)
            cv2.imshow('draw_obj', draw_Object)

        k = cv2.waitKey(10)

        if k == 27:  # press ESC to exit
            camera.release()
            cv2.destroyAllWindows()
            break
        elif k == ord('b'):
            bgModel = cv2.createBackgroundSubtractorMOG2(0, background_Subtract_Threshold)
            is_background_captured = 1
            print("capured")

        elif k == ord('r'):
            bgModel = None
            trigger_switch = False
            is_background_captured = 0
            print('reset')
        elif k == ord('k'):
            trigger_switch = True
            print("================ Trigger ON ================")
        elif k == ord('o'):
            trigger_switch = False
            print("================ Trigger OFF ================")