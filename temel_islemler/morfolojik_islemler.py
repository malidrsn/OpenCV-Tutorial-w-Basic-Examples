import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("klon.jpg", 0)  # 0 vermek siyah beyaz seçmek demek yani gray formata çeviriyor

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=5)
cv2.imshow("Original", img)
cv2.imshow("Erosion", erosion)

# ikinci yöntem
dilation = cv2.dilate(img, kernel, iterations=5)
cv2.imshow("Dilation", dilation)

# üçüncü yöntem open ve close fonksiyonları var. ayrıca gradient var,tophat var
opening = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Morfolojik", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
