import cv2
import numpy as np

cap = cv2.VideoCapture("4.1 line.mp4")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([18, 94, 140], np.uint8)  # sarı rengin alt ve üst noktaları internette bulunuor
    upper_yellow = np.array([48, 255, 255], np.uint8)  # hsv ranger for yellow diyerek ararız

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)  # maske görüntüyü ayırmak içindir.
    edges = cv2.Canny(mask, 75, 250)  # köşeleri verir

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)  # lineları buluyoruz

    for i in lines:
        x1, y1, x2, y2 = i[0]
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), thickness=2)  # lineleri çizdirme

    cv2.imshow("Mask", mask)
    cv2.imshow("Koseler", edges)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
