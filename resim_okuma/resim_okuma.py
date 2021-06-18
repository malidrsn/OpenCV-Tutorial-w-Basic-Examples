import cv2

img = cv2.imread("klon.jpg")
# print(img)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)  # pencere boyutlandırma

cv2.imshow("Image", img)  # resmi gösterme

cv2.imwrite("klon1.jpg", img)  # resmi başka bir dosya olarak yazma klonlama

cv2.waitKey(0)
cv2.destroyAllWindows()
