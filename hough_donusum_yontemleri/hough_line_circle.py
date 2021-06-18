# daireleri tespit etme saptama

import cv2
import numpy as np

img2 = cv2.imread("5.1 balls.jpg")
img1 = cv2.imread("5.2 coins.jpg")
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img1_blur = cv2.medianBlur(gray1, 5)  # 5 olan tek ve pozitif olmalı kernel size blur oranı gibi düşün
img2_blur = cv2.medianBlur(gray2, 5)  # gürültüyü kaldırıyor

circles = cv2.HoughCircles(img1_blur, cv2.HOUGH_GRADIENT,
                           1, img1.shape[0] / 4, param1=200,
                           param2=10, minRadius=15,
                           maxRadius=80)  # dp = çözürnürlük 1 olan ise çember bulma olayı için mesafe

if circles is not None:
    circles = np.uint16(np.around(circles))  # circlestan gelen değerleri yuvarlayıp tekrar circles'e atmak
    for i in circles[0, :]:
        cv2.circle(img1, (i[0], i[1]), i[2], (0, 255, 0), thickness=2)

cv2.imshow("img", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
