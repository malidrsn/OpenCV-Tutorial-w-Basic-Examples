# resim üzerinde ki gürültüleri azaltmayı sağlar. yumuşatma pürüzsüzlük sağlar

import cv2
import numpy as np

img_filter = cv2.imread("klon.jpg")
img_median = cv2.imread("klon.jpg")
img_bilateral = cv2.imread("klon.jpg")

blur = cv2.blur(img_filter,
                (11, 11))  # (5,5) resimin yumuşatma değeri pozitif tek sayi olmasi lazim arttıkça resim bulanıklaşır.
blur_gaussian = cv2.GaussianBlur(img_filter, (5, 5), cv2.BORDER_DEFAULT)

blur_median = cv2.medianBlur(img_median, 5)
blur_biliteral = cv2.bilateralFilter(img_bilateral, 9, 75, 75, )

cv2.imshow("Original", img_filter)
cv2.imshow("Blur", blur)
cv2.imshow("Gaussian Blur", blur_gaussian)
cv2.imshow("Median Blur", blur_median)
cv2.imshow("Bilateral Blur", blur_biliteral)

cv2.waitKey(0)
cv2.destroyAllWindows()
