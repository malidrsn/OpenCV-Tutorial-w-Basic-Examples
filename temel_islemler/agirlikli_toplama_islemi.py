# f(x,y) = x*q + y*b +c şeklinde olan formülasyon üzerinden işlenir. Birbirleri üzerine eklenir.
import cv2
import numpy as np

circle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.circle(circle, (256, 256), 60, (255, 0, 0), thickness=-1)
cv2.imshow("Circle", circle)

rectangle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(rectangle, (150, 150), (350, 350), (0, 255, 0), thickness=-1)
cv2.imshow("Rectangle", rectangle)

dst = cv2.addWeighted(circle, 0.7, rectangle, 0.3, 0)
cv2.imshow("DST", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
