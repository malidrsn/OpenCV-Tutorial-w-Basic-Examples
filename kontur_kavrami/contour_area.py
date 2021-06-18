import cv2

img = cv2.imread("5.2 contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Thresh", thresh)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # konturları bulma parametreler standart
cnt = contours[0]
# image moments için alan fonksiyonu
area = cv2.contourArea(cnt)  # contours kullanarak alan bulma
print(area)
M = cv2.moments(cnt)  # moments kullanarak alan bulma
print(M['m00'])
# alınan değerleri alarak alan ve çevre bulacaz

# çevre
perimeter = cv2.arcLength(cnt, True)  # çevre hesabı
print(perimeter)

cv2.waitKey(0)
cv2.destroyAllWindows()
