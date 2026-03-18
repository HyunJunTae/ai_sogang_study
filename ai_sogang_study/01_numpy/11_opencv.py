import cv2


# 1. 임계점 처리
images = []
image1 = cv2.imread("han.jpg", cv2.IMREAD_GRAYSCALE)
ret, thresh1 = cv2.threshold(image1, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(image1, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(image1, 127, 255, cv2.THRESH_TOZERO)
images.append(thresh1)
images.append(thresh2)
images.append(thresh3)

for i in images:
    cv2.imshow("original", i)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 2. 적응 임계점 처리
adaptive_images = []
thresh4 = cv2.adaptiveThreshold(image1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("original", thresh4)
cv2.waitKey(0)
cv2.destroyAllWindows()