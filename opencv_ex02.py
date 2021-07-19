import cv2

# simple OpenCV source
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320) # 창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) # 창 높이

fourcc = cv2.VideoWriter_fourcc(*'XVID')
is_record = False # 녹화상태

while True:
    ret, frame = cam.read()

    if ret:
        cv2.imshow('Original Video', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('c'): #c를　입력받으면
            cv2.imwrite('./capture/captured.jpg', frame)
            print('이미지 캡처 완료')
        elif key == ord('r') and is_record == False: #r : record
            is_record = True
            video = cv2.VideoWriter('./capture/record.avi', fourcc, 20, (frame.shape[1], frame.shape[0]))
            print('녹화시작')
        elif key == ord('r') and is_record == True: # recording
            is_record = False
            video.release()
            print('녹화종료')
        if is_record == True:
            video.write(frame)    

cam.release()
cv2.destroyAllWindows()