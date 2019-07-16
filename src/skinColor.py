import cv2
import numpy as np

cam = cv2.VideoCapture(0)

if __name__ == "__main__":
    while(1):
        ret , img = cam.read()

        cv2.rectangle(img,(400,400),(100,100),(0,255,0),0)
        crop_img = img[100:400,100:400]

        crop_img_hsv =cv2.cvtColor(crop_img,cv2.COLOR_BGR2HSV)
    
        lower_threshold = np.array([5, 48, 80], dtype=np.uint8)   #한계값
        upper_threshold = np.array([20, 255, 255], dtype=np.uint8)#한계값

        skin_grey = cv2.cvtColor(skin,cv2.COLOR_BGR2GRAY)
        _, thresh1 = cv2.threshold(skin_grey,157,235,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        thresh1_edges = cv2.Canny(thresh1,150,620)
        cv2.imshow('trt',thresh1)
        cv2.imshow('trt_canny',thresh1_edges)
        skinMask = cv2.inRange(crop_img_hsv, lower_threshold, upper_threshold)

        skinMask = cv2.GaussianBlur(skinMask, (5, 5), 0)

        skin = cv2.bitwise_and(crop_img_hsv, crop_img_hsv, mask=skinMask)

        skin = cv2.cvtColor(skin,cv2.COLOR_HSV2BGR)
        
        skin_grey = cv2.cvtColor(skin,cv2.COLOR_BGR2GRAY)
        _, thresh1 = cv2.threshold(skin_grey,157,235,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        thresh1_edges = cv2.Canny(thresh1,150,620)
        cv2.imshow('trt',thresh1)
        cv2.imshow('trt_canny',thresh1_edges)


        cv2.imshow('hsv',crop_img_hsv)
        cv2.imshow('img',img)
        cv2.imshow('skin',skin)
        end_out_key = cv2.waitKey(1)
        if end_out_key == 27:
            break

## 이미지 손 영역 임의 추출 까지 성공, 하지만 정확도가 낮아 다른 방법 필요할 것 같음