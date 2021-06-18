# transformation matrisi
import cv2
import numpy as np

img = cv2.imread("klon.jpg", 0)
row, col = img.shape

# trasformasyon matrisi

M = np.float32([[1, 0, 100], [0, 1, 100]])  # ilk değerler algoritmadan gelme diğer 100'ler itme mesafesi

dst = cv2.warpAffine(img, M, (row, col))

cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
