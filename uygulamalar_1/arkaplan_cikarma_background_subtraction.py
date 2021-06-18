import cv2
import numpy as np

cap = cv2.VideoCapture("5.1 car.mp4")
_, firstFrame = cap.read()
firstFrame = cv2.resize(firstFrame, (640, 480))

first_gray = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
first_blur = cv2.GaussianBlur(first_gray, (5, 5), 0)

while 1:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    diff = cv2.absdiff(first_gray, gray)  # karşılaştırma
    _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    cv2.imshow("Frame", frame)
    cv2.imshow("First Frame", firstFrame)
    cv2.imshow("Diff", diff)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
