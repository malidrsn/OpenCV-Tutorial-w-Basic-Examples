# region of interest --> ilgi alani
# yüz ile ilgileniyosak roi yüzdür
import cv2
import numpy as np

img = cv2.imread("klon.jpg")

cv2.imshow("Klon Asker ", img)

print(img.shape[:2])

roi = img[200:450, 300:500]
cv2.imshow("Roi : ", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
