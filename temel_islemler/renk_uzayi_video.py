import cv2
import numpy as np

capture = cv2.VideoCapture("MehmetAliDURSUN-202085151074.mp4")

while True:
    ret, frame = capture.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == False :
        break
    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
