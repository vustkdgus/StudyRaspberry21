import cv2

# simple OpenCV source
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320) # 창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) # 창 높이

while True:
    ret, frame = cam.read()

    if ret:
        cv2.imshow('Original Video', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

cam.release()
cv2.destroyAlWindows()