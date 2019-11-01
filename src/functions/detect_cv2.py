import cv2
import numpy as np
import copy
import math


learningRate = 0
background_Subtract_Threshold = 50
bgModel = None;

def remove_background(frame):
    fgmask = bgModel.apply(frame, learningRate=learningRate)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)  # 이미지 침식
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res

def CallBackFunction(event,x,y,flag,params):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print("x 좌표: ",x, "y 좌표", y)

def print_threshold(self):
    print("threshold = " + str(self))

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
                    #cv2.circle(drawing, end__, 8, [0, 211, 0], -1)
                    #cv2.circle(drawing, start__, 8, [0, 211, 0], -1)

            global hands_c
            hands_c  = cnt
            return True, cnt
        return False, 0
MX = 0
MY = 0

def draw____(img,MAX_x,MAX_y):
    global MX, MY
    MX = MAX_x
    MY = MAX_y
    cv2.rectangle(img, (0, 0), (int(MAX_x * 0.2), MAX_y), (100, 0, 255), 2);
    cv2.rectangle(img, (int(MAX_x * 0.8), 0), (MAX_x, MAX_y), (100, 0, 255), 2);
    cv2.rectangle(img, (int(MAX_x * 0.2), int(MAX_y * 0.62)), (int(MAX_x * 0.5), MAX_y), (255, 0, 255), 2);
    cv2.rectangle(img, (int(MAX_x * 0.5), int(MAX_y * 0.62)), (int(MAX_x * 0.8), MAX_y), (255, 0, 255), 2);

    return img
global cnt
cnt = 0
def return_compare(compare):
    global MX,MY
    global cnt, hands_c


    if(compare[0] > int(MX * 0.2) and compare[0] < int(MX * 0.5) and compare[1] > int(MY * 0.62) and compare[1] < MY) :
        cnt= cnt+1
        if(cnt >= 5):

            #return "section1_"+str(hands_c)
            return 1000
        else :
            pass
    if(compare[0] > int(MX * 0.5) and compare[0] < int(MX * 0.8) and compare[1] > int(MY * 0.62) and compare[1] < MY) :
        cnt= cnt+1
        if(cnt >= 5):

            #return "section2_"+str(hands_c)
            return 2000
        else :
            pass

    elif(compare[0] < int(MX * 0.2)) :
        cnt = cnt+1
        if(cnt >= 3):

            #return "left_"+str(hands_c)
            return 3000
        else :
            pass

    elif(compare[0] > int(MX * 0.8) and compare[0] < int(MX)) :
        if(cnt >= 5):

            #return "right_"+str(hands_c)
            return 4000
        else :
            pass

    else :
        if(cnt < 5): pass
        if(cnt >= 5):

            #return "none_"+str(hands_c)
            return 0