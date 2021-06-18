import cv2
import numpy as np

cap = cv2.VideoCapture("5.1 car.mp4")

subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=100,
                                                detectShadows=True)  # history frame sayısı
subtractor2 = cv2.createBackgroundSubtractorKNN(history=100, dist2Threshold=100, detectShadows=True)

while 1:

    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    mask = subtractor.apply(frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
