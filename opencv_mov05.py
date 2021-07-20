import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

#카메라 기본 툴
cap = cv2.VideoCapture(0) # 0 ~ 1
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# nanum gothic fonts
font = ImageFont.truetype('/fonts/NanumGothicBold.ttf', 20)

# infinite loop
while True:
    ret, frame = cap.read() # 카메라 현재 영상 로드, frame에　저장，　ret True/False
    h, w, _ = frame.shape
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')

    if ret != True: break # ret이 false면 루프탈출

    frame = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame)
    draw.text(xy=(10, (h-40)), text='실시간 웹캠 - {0}'.format(currDateTime), font=font, fill=(0, 0, 255))
    frame = np.array(frame)
    
    cv2.imshow('RealTime CAM', frame)
    if cv2.waitKey(1) == ord('q'):  break

cv2.release() # webcam 해제
cv2.destroyAllWindows()