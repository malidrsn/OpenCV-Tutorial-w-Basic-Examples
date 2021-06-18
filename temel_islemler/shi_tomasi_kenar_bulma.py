import cv2
import numpy as np

img = cv2.imread("1.png")
img1 = cv2.imread("2.jfif")

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)  # 100 olan bulunacak köşe sayısı

corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img1, (x, y), 3, (0, 0, 255), thickness=-1)

cv2.imshow("Corner", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
