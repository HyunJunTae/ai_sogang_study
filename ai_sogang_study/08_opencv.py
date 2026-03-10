import cv2

# 1. 이미지 불러와서 출력
image = cv2.imread("jang.jpg", cv2.IMREAD_COLOR)
cv2.imshow("1", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. 이미지 특정 픽셀 변경
image[300:400, 450:800] = [0,0,0]
cv2.imshow("2", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. 특정 픽셀 복사 & 출력
ROI = image[300:400, 450:800]
cv2.imshow("3", ROI)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. 복사한 특정 픽셀 붙여넣기
image[0:100, 0:350] = ROI
cv2.imshow("4", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. 색상 설정
image[:, :, 2] = 0 # 전체 행(높이), 전체 열(너비)에 대해서 빨간색(2)에 해당하는 값을 0으로 설정
cv2.imshow("5", image)
cv2.waitKey(0)
cv2.destroyAllWindows()



han_image = cv2.imread("han.jpg", cv2.IMREAD_COLOR)
han_ROI = han_image[140:155, 325:350]
han_image[125:140, 305:330] = han_ROI
cv2.imshow("6", han_image)
cv2.waitKey(0)