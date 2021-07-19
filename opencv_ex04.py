import cv2
import numpy as np

org = cv2.imread('./image/cat.jpg', cv2.IMREAD_GRAYSCALE)
dst = cv2.resize(org, dsize=(640, 480))

center = [340, 270] # x, y
color = (0, 0, 255) # red

cv2.rectangle(dst, (100, 100), (500, 300), (255, 0, 0))
cv2.circle(dst, center, 30, color)


cv2.imshow("dest", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()