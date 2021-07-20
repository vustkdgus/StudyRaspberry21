import cv2
import numpy as np

#이미지 대비
##
org = cv2.imread('./image/cat.jpg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
ret, bny = cv2.threshold(gray, 127, 255, 0)
cont, hirc = cv2.findContours(bny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(org, cont, 0, (0, 255, 0), 2)
cv2.imshow('Thr', bny)
cv2.imshow('Result', org)

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() # 메모리 해제
