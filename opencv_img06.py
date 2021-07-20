import cv2
import numpy as np

#이미지 대비
org = cv2.imread('./image/cat.jpg')
enhanced = cv2.equalizeHist(org)

cv2.imshow('original', org) #cv2 새창 열림
cv2.imshow('Enhanced', enhanced)

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() # 메모리 해제
