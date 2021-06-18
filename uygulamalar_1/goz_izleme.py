import cv2
import numpy as np

cap = cv2.VideoCapture("15.1 eye_motion.mp4")

while 1:
    ret, frame = cap.read()  # ret burada true yada false dönderiyor frameler gelmiş olma durumuna göre

    if ret is False:
        break

    roi = frame[80: 210, 230: 450]
    rows, cols, _ = roi.shape
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 2, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for i in contours:
        (x, y, w, h) = cv2.boundingRect(
            i)  # koordinat değerlerini alıyor bu fonksiyon. contours'un ilk değerini alıp köşeleri belirliyor
        cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)
        break
    frame[80: 210, 230: 450] = roi
    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Threshold", thresh)

    if cv2.waitKey(80) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
