# convexhull dış bükey geometrik şekildir. iç bükey şekillere dış bükey örtüler çizmektir amacı
# convexity defects dışbükey kusurlardır.
# konturlar bir resmin sınır çizgileridir
import cv2

img = cv2.imread("2.1 contour1.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)  # default olarak kullanılır. daha düzgün çıkması için

cv2.drawContours(img, contours, 1, (0, 0, 255),
                 3)  # 1 olan kısım -1 yazarsak çerçeveyi de çizer 0 yazarsak sadece çerçever çizer

cv2.imshow("Kontur", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
