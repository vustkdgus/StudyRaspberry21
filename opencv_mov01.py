import cv2
import numpy as np

#카메라 기본 툴
cap = cv2.VideoCapture(0) # 0 ~ 1
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# infinite loop
while True:
    ret, frame = cap.read() # 카메라 현재 영상 로드, frame에　저장，　ret True/False

    if ret != True: break # ret이 false면 루프탈출
    
    cv2.imshow('RealTime CAM', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.release() # webcam 해제
cv2.destroyAllWindows()