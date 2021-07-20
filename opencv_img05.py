import cv2
import numpy as np

#add noise
org = cv2.imread('./image/cat.jpg')
h, w, c = org.shape
noise = np.uint8(np.random.normal(loc=0, scale=0.4, size=[h, w, c]))
noised_img = cv2.add(org, noise) # add noise at org

cv2.imshow('original', org) #cv2 새창 열림
cv2.imshow('Noise', noised_img)

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() # 메모리 해제
