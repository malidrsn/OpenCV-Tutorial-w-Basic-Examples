import cv2
import numpy as np

img = cv2.imread("1.png")

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    edges = cv2.Canny(frame, 100, 200)

    cv2.imshow("Orjinal", frame)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
