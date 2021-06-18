import cv2
import numpy as np

img = cv2.imread("klon.jpg")

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR'dan RGB'ye çevirme

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR'dan HSV'ye çevirme

img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # BGR'dan Gray'e çevirme

cv2.imshow("Klon Asker BGR", img)
cv2.imshow("Klon Asker RGB", img1)
cv2.imshow("Klon Asker HSV", img2)
cv2.imshow("Klon Asker GRAY", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
