# gruplandırma yapabilir
# thresholding yapmak için resmi grayscale yapmak lazim
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("klon.jpg", 0)  # 0 vermek siyah beyaz seçmek demek yani gray formata çeviriyor

ret, th1 = cv2.threshold(img, 100, 200, cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)  # daha sonra bu

th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)  # en mantıklısı bu gibi
cv2.imshow("img", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
