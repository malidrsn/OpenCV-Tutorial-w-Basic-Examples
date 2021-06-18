# image filter da denir. bir şeklin geometrik merkezi vs bulunmaktadır.
import cv2

img = cv2.imread("5.2 contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# cv2.moment bazı sözlük değerleri saklıyor göörüntü ile alakalı
M = cv2.moments(thresh)

# geometri merkezini bulmaya çalışıyoruz bunun için mo1,m00,m10 kullanacaz

X = int(M["m10"] / M["m00"])  # ağırlık merkezi x noktasi
Y = int(M["m01"] / M["m00"])  # y noktasi

cv2.circle(img, (X, Y), 5, (0, 0, 255), -1)  # img penceresine ağırlık merkezi olan bir circle yerleştiriyoruz

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
