import cv2
import numpy as np


# 이미지 합치기

image1 = cv2.imread("han.jpg", cv2.IMREAD_COLOR)
image2 = cv2.imread("han.jpg", cv2.IMREAD_COLOR)

result1 = cv2.add(image1, image2)
cv2.imshow("result", result1)
cv2.waitKey(0)
cv2.destroyAllWindows()

result2 = np.add(image1, image2)
cv2.imshow("result", result2)
cv2.waitKey(0)
cv2.destroyAllWindows()