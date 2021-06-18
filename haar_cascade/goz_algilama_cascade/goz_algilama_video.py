import cv2
import numpy as np

cascade_faces = cv2.CascadeClassifier("4.3 frontalface.xml")

cascade_eyes = cv2.CascadeClassifier("5.1 eye.xml")

cap = cv2.VideoCapture("10.3 eye.mp4")

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = cascade_faces.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 3)

    roi_frame = frame[y:y + h, x:x + w]
    roi_gray = gray[y:y + h, x:x + w]

    eyes = cascade_eyes.detectMultiScale(roi_gray)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 3)

    cv2.imshow("Frames", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
