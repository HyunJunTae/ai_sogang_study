import cv2

# 이미지 읽어오기.
img_basic = cv2.imread("jang.jpg", cv2.IMREAD_COLOR)

# 이미지 출력하기. waitKey로 어떠한 키 입력이 있을 때까지 프로그램 대기
cv2.imshow("Basic", img_basic)
cv2.waitKey(0)

# 읽어온 이미지 새로운 파일로 저장히기
cv2.imwrite("new_jang.jpg", img_basic)

# 모든 창 닫기
cv2.destroyAllWindows()



# 읽어온 이미지로 새로운 이미지 생성. COLOR_BGR2GRAY로 회색으로 생성.
img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow("Basic", img_gray)
cv2.waitKey(0)
cv2.imwrite("new_new_jang.jpg", img_gray)