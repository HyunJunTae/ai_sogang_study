import cv2
import numpy as np

# 1. 기본 이미지 입력, 보여주기
image = cv2.imread("jang.jpg")
cv2.imshow("1", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. 이미지 확대
expanded_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("2", expanded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. 이미지 축소
shrank_image = cv2.resize(image, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
cv2.imshow("3", shrank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. 이미지 위치 옮기기
height, width = image.shape[:2]

M = np.float32([[1, 0, 50], [0, 1, 10]]) # 변환 행렬 사용. 가로로 50px, 세로로 10px 만큼.
moved_image = cv2.warpAffine(image, M, (width, height))
cv2.imshow("4", moved_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 5. 이미지 회전
height, width = image.shape[:2]

M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5) # 반시계방향 90도, 0.5배 크기.
rotated_image = cv2.warpAffine(image, M, (width, height))
cv2.imshow("5", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

