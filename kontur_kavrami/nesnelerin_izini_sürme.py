import cv2
import numpy as np

cap = cv2.VideoCapture("4.1 dog.mp4")

while 1:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    sensitivity = 15
    lower_white = np.array([0, 0, 255 - sensitivity])  # beyaz arama
    upper_white = np.array([255, sensitivity, 255])  # kırmızı arama için hsv code for red diye aramak lazım

    mask = cv2.inRange(hsv, lower_white, upper_white)  # bu aralıklara maske uygula geri kalanını kazı anlamına gelir
    res = cv2.bitwise_and(frame, frame, mask=mask)  # and işlemi yapmakta maske için

    cv2.imshow("Frame ", frame)
    cv2.imshow("Mask ", mask)
    cv2.imshow("Result ", res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
