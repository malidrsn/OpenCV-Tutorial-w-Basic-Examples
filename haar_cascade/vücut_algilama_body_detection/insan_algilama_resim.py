import cv2
import numpy as np

img = cv2.imread("3.3 body.jpg")
body_cascade = cv2.CascadeClassifier("3.1 fullbody.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bodies = body_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
