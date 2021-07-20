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
# codec
fourcc = cv2.VideoWriter_fourcc(*'XVID') # H263
is_record = False

# infinite loop
while True:
    ret, frame = cap.read() # 카메라 현재 영상 로드, frame에　저장，　ret True/False
    h, w, _ = frame.shape
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    fileDateTime = now.strftime('%Y%m%d_%H%M%S')

    if ret != True: break # ret이 false면 루프탈출

    frame = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame)
    draw.text(xy=(10, (h-40)), text='실시간 웹캠 - {0}'.format(currDateTime), font=font, fill=(0, 0, 255))
    frame = np.array(frame)
    
    cv2.imshow('RealTime CAM', frame)
    key = cv2.waitKey(1)
    if key == ord('q'): break
    elif key == ord('c'):
        cv2.imwrite('./capture/img_{0}.png'.format(fileDateTime), frame)
        print('이미지 저장 완료')
    elif key == ord('r'): # record
        is_record = True
        video = cv2.VideoWriter('./capture/record_{0}.avi'.format(fileDateTime), fourcc, 20, (w, h))
        print('녹화 시작')
    elif key == ord('t'): # end record
        is_record = False
        if 'video' in locals():
            video.release() # 객체해제
            print('녹화 완료')

    if is_record:
        video.write(frame)
        cv2.circle(img=frame, center=(620, 15), radius=5, color=(0,0,255), thickness=3)

cv2.release() # webcam 해제
cv2.destroyAllWindows()