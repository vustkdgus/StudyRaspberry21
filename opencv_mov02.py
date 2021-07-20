import cv2
import numpy as np

#카메라 기본 툴
cap = cv2.VideoCapture(0) # 0 ~ 1
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# infinite loop
while True:
    ret, frame = cap.read() # 카메라 현재 영상 로드, frame에　저장，　ret True/False
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret != True: break # ret이 false면 루프탈출
    
    cv2.imshow('RealTime CAM', frame)
    cv2.imshow('Gray Result', gray)

    if cv2.waitKey(1) == ord('q'):  break

cv2.release() # webcam 해제
cv2.destroyAllWindows()