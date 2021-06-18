import cv2
import numpy as np

cap = cv2.VideoCapture("6.2 body.mp4")
body_cascade = cv2.CascadeClassifier("3.1 fullbody.xml")

while 1:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bodies = body_cascade.detectMultiScale(gray, 1.4, 5)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
