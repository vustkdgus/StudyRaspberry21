import cv2
import numpy as np

#image load simple frame
##image blur
org = cv2.imread('./image/cat.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(org, (10, 10))
kernel = np.array([[0, -1, 0], [-1,5,-1],[0,-1,0]])
sharp = cv2.filter2D(org, -1, kernel)

cv2.imshow('Original', org) #cv2 새창 열림
cv2.imshow('Blur', blur) #image blur window
cv2.imshow('Kernel', kernel) #image blur window

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() # 메모리 해제
