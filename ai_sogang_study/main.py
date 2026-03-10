import cv2

img_basic = cv2.imread("jang.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Basic", img_basic)
cv2.waitKey(0)
cv2.imwrite("new_jang.jpg", img_basic)


cv2.destroyAllWindows()

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow("Basic", img_gray)
cv2.waitKey(0)
cv2.imwrite("new_new_jang.jpg", img_gray)