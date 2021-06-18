import cv2
import numpy as np

cap = cv2.VideoCapture("traffic.avi")

backsub = cv2.createBackgroundSubtractorMOG2()  # arka plan

sayac = 0

while 1:
    ret, frame = cap.read()
    if ret:
        foregroundMask = backsub.apply(frame)

        cv2.line(frame, (50, 0), (50, 300), (0, 255, 0), thickness=2)
        cv2.line(frame, (70, 0), (70, 300), (0, 255, 0), thickness=2)

        contours, hierarchy = cv2.findContours(foregroundMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        try:
            hierarchy = hierarchy[0]
        except:
            hierarchy = []

        for contour, hier in zip(contours, hierarchy):
            (x, y, w, h) = cv2.boundingRect(contour)
            if w > 40 and h > 40:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=3)
                if x > 50 and x < 70:
                    sayac += 1
        cv2.putText(frame, "Car :" + str(sayac), (90, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), thickness=2,
                    lineType=cv2.LINE_AA)
        cv2.imshow("Counter", frame)

        cv2.imshow("img", foregroundMask)

        if cv2.waitKey(20) & 0xFF == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()
