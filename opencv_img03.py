import cv2
import numpy as np

#
org = cv2.imread('./image/cat.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

h, w, c = org.shape

cropped = gray[:int(h/2), :int(w/2)]
# cropped = org[:int(h/2), :int(w/2)]

cv2.imshow('Original', org) #cv2 새창 열림
cv2.imshow('Crop', cropped)

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() # 메모리 해제
