import cv2
import numpy as np

img = cv2.imread("5.3 eye.png")

cascade_faces = cv2.CascadeClassifier("4.3 frontalface.xml")
cascade_eyes = cv2.CascadeClassifier("5.1 eye.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cascade_faces.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

img2 = img[y:y + h, x:x + w]
gray2 = gray[y:y + h, x:x + w]

eyes = cascade_eyes.detectMultiScale(gray2)

for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(img2, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
